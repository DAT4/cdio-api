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
    img = cv.imdecode(img, cv.IMREAD_COLOR)
    img = resize(img)
    return core.extractCornor(core.findCard(img))


def save(img):
    is_success, buffer = cv.imencode(".jpg", img)
    return io.BytesIO(buffer)
