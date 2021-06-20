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
    dimensions  = get_dimensions(contours)
    draw_contours_on_image(img, dimensions)
    objects     = get_objects(gray, dimensions)
    return get_final_object(objects)


def get_final_object(objects):
    if len(objects) == 2:
        a,b = objects
        return cv.resize(np.hstack((b,a)),(10,10))
    return objects[0]


def get_dimensions(contours):
    return [cv.boundingRect(cnt)
        for cnt
        in contours
        if cv.contourArea(cnt) > 50]


def get_objects(img, dimensions):
    return [get_object(img, (x,y,w,h))
        for [x,y,w,h]
        in dimensions
        if h>20]


def draw_contours_on_image(img, dimensions):
    for [x,y,w,h] in dimensions:
        if h>20: cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)


def get_object(img, dim):
    [x, y, w, h] = dim
    out = cv.resize(img[y:y+h,x:x+w],(10,10))
    _, out = cv.threshold(out, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)
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
    gray        = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    _, thresh   = cv.threshold(gray, 140, 255, cv.THRESH_BINARY)

    contours    = cv.findContours(image=thresh.copy(), mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
    contours    = util.grab_contours(contours)
    contours    = sorted(contours,key=cv.contourArea,reverse=True)[:3]

    return get_card(contours, img)


def get_card(contours, img):
    for cnt in contours:
        aprox = get_aprox(cnt)
        if is_card(aprox):
            return extract_card(aprox, img)
    return None


def get_aprox(cnt):
    lnked = cv.arcLength(cnt,True)
    return cv.approxPolyDP(cnt,0.02*lnked,True)


def is_card(aprox):
    return len(aprox) == 4


'''
extract_cornor() takes the extracted card as a parameter
the function returns the number and symbol
'''
def extract_cornor(card):
    corner = card[0:80,0:30]
    num, sym = strip_margin(corner[:45]), strip_margin(corner[40:])
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
    h,w,_ = img.shape
    w, h, = w//7, h//2
    return [img[i*h:i*h+h,j*w:j*w+w]
            for i in range(2)
            for j in range(7)
            if is_card_pos(i,j)]


