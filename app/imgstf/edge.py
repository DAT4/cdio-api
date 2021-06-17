import io
import cv2 as cv
import numpy as np

from . import core, dao

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

def get_num_and_sym(corner, db_syms, db_nums):
    num, sym = corner
    return check_sym(sym, db_syms) + check_num(num, db_nums)

def gamestatify(liste):
    out = {
            'builds': liste[:7],
            'suits': liste[-4:],
            'deck': liste[-5],
            }
    print(out)
    return out

class ImageMachine:
    def __init__(self, db):
        self.db = db

    def gamestate_from_board(self, file):
        corners = [core.extract_cornor(core.find_card(x))
                for x in core.split_board(load(file))]
        db_syms = self.db.get_all_syms()
        db_nums = self.db.get_all_nums()
        liste = [get_num_and_sym(x, db_syms, db_nums) for x in corners]
        return gamestatify(liste)
