import cv2 as cv
import numpy as np
import imutils as util

'''
strip_margin() should get a part of the corner in the parameters
the function removes the margin around the symbol (num or suit)
and returns a 10x10 pixel binary representation of the symbol
'''
def strip_margin(img):
    gray        = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    blur        = cv.GaussianBlur(gray,(5,5),0)
    thresh      = cv.adaptiveThreshold(blur,255,1,1,11,2)
    contours,_  = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    return get_objects(gray, contours)[0]

def get_contours(contours):
    return [cnt
        for cnt
        in contours
        if cv.contourArea(cnt) > 50]

def get_objects(img, contours):
    return [get_object(img, x,y,w,h)
        for [x,y,w,h]
        in [cv.boundingRect(cnt)
        for cnt
        in get_contours(contours)]
        if h>20]

def get_object(img, x, y, h, w):
    a = img[y:y+h,x:x+w]
    b = cv.resize(a,(10,10))
    _, out = cv.threshold(b, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)
    return out


'''
extract_card() takes the contours and the image of a card as the parameters
the function applies the contours to the original image and warps it into an
right-angled shape.
the warped image is returned
'''
def extract_card(aprox,img):
    pts1 = aprox.reshape(4, 2)
    rect = np.zeros((4, 2), dtype="float32")
    s = pts1.sum(axis=1)
    rect[0] = pts1[np.argmin(s)]
    rect[3] = pts1[np.argmax(s)]

    diff = np.diff(pts1, axis=1)
    rect[1] = pts1[np.argmin(diff)]
    rect[2] = pts1[np.argmax(diff)]

    pts2 = np.float32([[0, 0], [200, 0], [0, 300], [200, 300]])
    matrix = cv.getPerspectiveTransform(rect, pts2)
    result = cv.warpPerspective(img, matrix, (200, 300))
    return result


'''
find_card() takes the original image as the parameter
the function finds the contours shaping the card
and returns extract_card() on the image with the found contours
'''
def find_card(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    _, thresh = cv.threshold(gray, 140, 255, cv.THRESH_BINARY)
    see = cv.findContours(image=thresh.copy(), mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
    see = util.grab_contours(see)
    see = sorted(see,key=cv.contourArea,reverse=True)[:3]
    for s in see:
        lnked = cv.arcLength(s,True)
        aprox = cv.approxPolyDP(s,0.02*lnked,True)
        if len(aprox) == 4:
            print('found card')
            return extract_card(aprox,img)


'''
extract_cornor() takes the extracted card as a parameter
the function returns the number and symbol
'''
def extract_cornor(card):
    corner = card[0:80,0:30]
    num, sym = strip_margin(corner[:40]), strip_margin(corner[40:])
    return num, sym


'''
split_board() takes the first image sent from the phone in the
scale 1:2.5 landscape
the function returns an array of single card images, in order.

|---------------|
| # # # # # # # |
|               |
| #     # # # # |
|---------------|
'''
def split_board(img):
    def is_card_pos(i,j): return i!=1 or j!=1 and j!=2
    w, h, b = 560, 800, 15
    return [img[b+i*h:b+i*h+h,b+j*w:b+j*w+w]
            for i in range(2)
            for j in range(7)
            if is_card_pos(i,j)]


'''
show() takes an image, shows it and returns the ascii value of
a key pressed while focusing the window
'''
def show(img):
    cv.imshow('hej', img)
    return cv.waitKey(0)

def get(path):
    return cv.cvtColor(cv.imread(path), cv.COLOR_BGR2RGB)
