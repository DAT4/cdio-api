import io
import cv2 as cv
import numpy as np
from models.gamestate import GameState
from . import core

def load(file):
    '''Loads image from byearray'''
    img = np.asarray(bytearray(file.read()), dtype="uint8")
    return cv.imdecode(img, cv.IMREAD_COLOR)

def save(img):
    '''returns image as byte array'''
    is_success, buffer = cv.imencode(".jpg", img)
    return io.BytesIO(buffer)

def get_card(img):
    '''returns card object from image'''
    card_img = core.find_card(img)
    return core.create_card_object(card_img)

def gamestate_from_board(self, db, board_image):
    '''returns gamestate object from image of board'''
    cards = [im.get_card(x)
            for x
            in core.split_board(board_image)]
    return GameState(db, cards)

def show(img):
    '''shows image'''
    cv.imshow('hej', img)
    return cv.waitKey(0)

def get(path):
    '''loads image from path'''
    return cv.cvtColor(cv.imread(path), cv.COLOR_BGR2RGB)
