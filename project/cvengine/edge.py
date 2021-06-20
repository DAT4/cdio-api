import io
import cv2 as cv
import numpy as np

from . import core


def resize(img):
    desired_size = 300
    old_size = img.shape[:2]
    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
    return cv.resize(img, (new_size[1], new_size[0]))

def load(file):
    img = np.asarray(bytearray(file.read()), dtype="uint8")
    return cv.imdecode(img, cv.IMREAD_COLOR)

def save(img):
    is_success, buffer = cv.imencode(".jpg", img)
    return io.BytesIO(buffer)

def check_num(img, image_nums):
    lowest = 100
    out = None
    for im in image_nums:
        name = im['name']
        im = im['number']
        im = cv.cvtColor(im, cv.COLOR_GRAY2BGR)
        im = cv.cvtColor(im, cv.COLOR_RGB2GRAY)
        bit = cv.bitwise_xor(img, im)
        count = find_white_pixels(bit)
        if count < lowest:
            lowest = count
            out = {'name':name,'bit':bit}
    return out['name']

def check_sym(img, image_syms):
    lowest = 100
    out = None
    for im in image_syms:
        name = im['name']
        im = im['symbol']
        im = cv.cvtColor(im, cv.COLOR_GRAY2BGR)
        im = cv.cvtColor(im, cv.COLOR_RGB2GRAY)
        bit = cv.bitwise_xor(img, im)
        count = find_white_pixels(bit)
        if count < lowest:
            lowest = count
            out = {'name':name,'bit':bit}
    return out['name']

def find_white_pixels(img):
    out = 0
    for x in img:
        for y in x:
            if y != 0:
                out += 1
    return out

def get_the_stuff(img):
    card = core.find_card(img)
    num, sym = core.extract_cornor(card)
    return {
            'card': card,
            'num': num,
            'sym': sym,
            }


def get_num_and_sym(corner, syms, nums):
    num, sym = corner
    return check_sym(sym, syms) + check_num(num, nums)

def gamestatify(liste):
    out = {
            'builds': liste[:7],
            'suits': liste[-4:],
            'deck': liste[-5],
            }
    return out

def cards_from_list(imglist):
    return [core.find_card(x) for x in imglist]

def split_board(img):
    return core.split_board(img)

def cards_from_path_list(pathlist):
    return [core.find_card(get(x)) for x in pathlist]

class ImageMachine:
    def __init__(self, db):
        self.db = db

    def gamestate_from_board(self, file):
        corners = [core.extract_cornor(x)
                for x in cards_from_board(load(file))]
        db_syms = self.db.get_all_syms()
        db_nums = self.db.get_all_nums()
        return gamestatify([get_num_and_sym(x, db_syms, db_nums) for x in corners])

'''
show() takes an image, shows it and returns the ascii value of
a key pressed while focusing the window
'''
def show(img):
    cv.imshow('hej', img)
    return cv.waitKey(0)

def get(path):
    return cv.cvtColor(cv.imread(path), cv.COLOR_BGR2RGB)

board = get('resources/boards/out/2.jpg')
