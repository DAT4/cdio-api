from flask import Flask, request
import cv2 as cv
import imgstuff
import numpy as np


app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    print('hello image man')
    image = request.files['image']
    image.save('download.jpg')
    imgstuff.useImage('download.jpg')
    return ("ok", 300)



if __name__ == '__main__':
    app.run(debug=True, port=1234)
