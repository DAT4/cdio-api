from flask import Flask, request
import cv2 as cv
import imgstuff
import numpy as np
import uuid


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    image = request.files['image']
    name = uuid.uuid4()
    image.save(f'uploads/{name}.jpg')
    if imgstuff.testSave(f'{name}.jpg'):
        return (f'http://mama.lan:1234/dl?corner={path}', 200)
    return (f'fejl', 500)


@app.route('/image/', methods=['POST'])
def get_image():
    card = request.args.get('card')
    corner = request.args.get('corner')
    if card:
        return app.send_static_file(f'downloads/cards/{card}.jpg')
    elif corner:
        return app.send_static_file(f'downloads/corners/{corner}.jpg')
    else:
        return 'fejl', 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1234)
