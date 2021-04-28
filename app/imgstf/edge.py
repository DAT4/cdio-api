import io
import cv2 as cv
import numpy as np

from . import core

def load(file):
    img = np.asarray(bytearray(file.read()), dtype="uint8")
    img = cv.imdecode(img, cv.IMREAD_COLOR)
    return core.extractCornor(core.findCard(img))


def save(img):
    is_success, buffer = cv.imencode(".jpg", img)
    return io.BytesIO(buffer)
