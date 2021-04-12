import os
import cv2 as cv
import numpy as np
import imutils as util
import database
import uuid

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
    cornor = card[0:80,1:25]
    cornor = cv.cvtColor(cornor,cv.COLOR_RGB2GRAY)
    _, cornor = cv.threshold(cornor, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)
    return cornor


def findCard(img):
    '''Will find the squares in the full image and extract a single card'''
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
            return extractCard(aprox,img)

def findWhitePixels(img):
    out = 0 
    for x in img:
        for y in x:
            if y != 0:
                out += 1
    return out

def compareImg(img):
    for card in database.get_all():
        image = card['image']
        image = cv.cvtColor(image, cv.COLOR_GRAY2BGR)
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        bit = cv.bitwise_xor(img, image)
        cv.imshow('bit', bit)
        print(findWhitePixels(bit))



def showCard(img):
    card = findCard(img)
    #cv.imshow(f'{uuid.uuid4()} card', card)
    cornor = extractCornor(card)
    cv.imshow(f'{uuid.uuid4()} corner', cornor)

def done():
    cv.waitKey()
    cv.destroyAllWindows()

def divideDeckAndSaveToDB():
    #This function is used to divide a deck of card into separate cards
    img = cv.imread('deck.png')
    w = 390
    h = 570
    b = 15

    sym = ['spade', 'heart', 'diamond', 'clubs']
    num = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'knight', 'queen', 'king',]

    for i in range(4):
        for j in range(13):
            corner = extractCornor(findCard(img[b+i*h:b+i*h+h,b+j*w:b+j*w+w]))
            database.save_img(
                num[j],
                sym[i],
                corner
                )


def testShowDB():
    #Wrong cards in database
    for card in database.get_all():
        cv.imshow('hej',card['image'])
        done()

def testCompare():
    for path in os.listdir('resources'):
        img = cv.imread(f'resources/{path}')
        card = findCard(img)
        if card is not None:
            corner = extractCornor(card)
            compareImg(corner)
            done()

if __name__ == '__main__':
    testCompare()

