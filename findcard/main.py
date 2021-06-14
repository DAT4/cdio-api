import cv2 as cv
import numpy as np
from core import *


def recognize(self, img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    thresh = cv.adaptiveThreshold(gray,255,1,1,11,2)
    contours,_ = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv.contourArea(cnt)>50:
            [x,y,w,h] = cv.boundingRect(cnt)
            if  h>20:
                cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                roi = thresh[y:y+h,x:x+w]
                roismall = cv.resize(roi,(10,10))
                show(roismall)
                roismall = roismall.reshape((1,100))
                roismall = np.float32(roismall)
                _, results, _, _= model.findNearest(roismall, k = 1)
                string = str(int((results[0][0])))
                cv.putText(out,string,(x,y+h),0,1,(0,255,0))
            return out

def find_somthing(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray,(5,5),0)
    thresh = cv.adaptiveThreshold(blur,255,1,1,11,2)
    contours,_ = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv.contourArea(cnt)>50:
            [x,y,w,h] = cv.boundingRect(cnt)
            if  h>20:
                cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                roi = gray[y:y+h,x:x+w]
                roismall = cv.resize(roi,(10,10))
                _, roismall = cv.threshold(roismall, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)
                return roismall

if __name__=='__main__':
    img = cv.imread('board.jpg')
    x = split_board(img)
    print(len(x))
    for x in x:
        card = find_card(x)
        num, suit = extract_cornor(card)
        d = find_somthing(num)
        cv.imshow('hej', d)
        cv.waitKey(0)