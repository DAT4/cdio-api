import cv2 as cv
from core import *
from os import listdir


def get_bgr(path):
    return cv.imread(path)

def show(img):
    cv.imshow('hej', img)
    return cv.waitKey(0)

def testing_board(image):

    show(image)

    images = split_board(image)

    for img in images:
        #show(img)
    
        image = find_card(img)
        t, b = extract_cornor(image)

        show(image)
        show(t)
        show(b)

def testing_find_card_with_cornor(img):
    image = find_card(img)
    t, b = extract_cornor(image)

    show(image)
    show(t)
    show(b)

def testing_find_card(img):
    image = find_card(img)
    t, b = extract_cornor(image)

    show(image)

image = get_bgr('/home/thomas/Skrivebord/Projects/Mapper/OpenCV/cdio-api/gui/boards/out/out.jpg')
hj = get_bgr('/home/thomas/Skrivebord/Projects/Mapper/OpenCV/cdio-api/gui/new/20210617_105545.jpg')
cj = get_bgr('/home/thomas/Skrivebord/Projects/Mapper/OpenCV/cdio-api/gui/new/20210617_105410.jpg')
qs = get_bgr('/home/thomas/Skrivebord/Projects/Mapper/OpenCV/cdio-api/gui/new/20210617_105313.jpg')

path = '/home/thomas/Skrivebord/Projects/Mapper/OpenCV/cdio-api/gui/new'
images  = [f'{path}/{x}'for x in listdir(path) if x[-3:] == 'jpg']

#testing_find_card_with_cornor(qs) 


for img in images:
    image = get_bgr(img)
    testing_find_card(image)


'''
appen er sat til            = 1800*4000

Emulator tager billeder i   = 324*720

Et eller andet 3.           = 410*1280

Noget 4.                    = 512*1280

/home/thomas/Skrivebord/Projects/Mapper/OpenCV/cdio-api/gui/new/20210617_105410.jpg
'''