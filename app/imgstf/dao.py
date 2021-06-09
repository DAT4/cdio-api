import os
import database.database as db
import uuid
import cv2 as cv

#TODO refactor 


def compareImg(img):
    for card in db.get_all():
        print(card['symbol'],card['number'])
        image = card['image']
        image = cv.cvtColor(image, cv.COLOR_GRAY2BGR)
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        bit = cv.bitwise_xor(img, image)
        cv.imshow('bit', bit)
        print(findWhitePixels(bit))


def findWhitePixels(img):
    out = 0 
    for x in img:
        for y in x:
            if y != 0:
                out += 1
    return out
