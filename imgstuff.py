import cv2 as cv
import numpy as np
import imutils as util
import database

def extractCard(aprox,img):
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
    

def extractCornor(card):
    cornor = card[0:70,1:25]
    cornor = cv.cvtColor(cornor,cv.COLOR_RGB2GRAY)
    _, cornor = cv.threshold(cornor, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)
    return cornor


def saveCornor(cornor):
    sym = input("SYMBOL: ")
    num = input("NUMBER: ")
    database.save_img(num, sym, cornor)


def findCard(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    squere = cv.Canny(gray,150,150)
    k = np.ones([2,2],np.uint8)
    squere = cv.dilate(squere,k,iterations=2)

    see = cv.findContours(squere.copy(),cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    see = util.grab_contours(see)
    see = sorted(see,key=cv.contourArea,reverse=True)[:3]

    for s in see:
        lnked = cv.arcLength(s,True)
        aprox = cv.approxPolyDP(s,0.02*lnked,True)

        if len(aprox) == 4:

            result = extractCard(aprox,img)
            cornor = extractCornor(result)

            cv.imshow(f"Cornor{s}", cornor)
            compareImg(cornor)
            #saveCornor(cornor)
            #cv.imshow(f"Perspective{s}",result)
            #cv.drawContours(img,[aprox],-1,(0,255,0),2)

    #cv.imshow("Video",img)

def useWebCam():
    cap = cv.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    cap.set(10,100)

    while True:
        success, img = cap.read()
        findCard(img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break


def useImage(imagePath):
    img = cv.imread(imagePath)
    print('hello image inside')
    findCard(img)
    cv.waitKey()
    cv.destroyAllWindows()


def compareImg(img):
    #NOTE: Find out how to make image array into binary format

    #fourofhearts = cv.imread("saved/fourofhearts.png")
    #fourofhearts = cv.cvtColor(fourofhearts, cv.COLOR_RGB2GRAY)

    #aceofspace = cv.imread("saved/aceofspace.png")
    #aceofspace = cv.cvtColor(aceofspace, cv.COLOR_RGB2GRAY)

    for card in database.get_all():
        image = card['image']
        image = cv.cvtColor(image, cv.COLOR_GRAY2BGR)
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        bit = cv.bitwise_xor(img, image)
        cv.imshow('bit', bit)
        print(true(bit))


def true(img):
    out = 0 
    for x in img:
        for y in x:
            if y != 0:
                out += 1
    return out

if __name__ == '__main__':
    useImage('ace.jpg')
    #useWebCam()

