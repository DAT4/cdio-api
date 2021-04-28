from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

import cv2 as cv
import imgstuff
import numpy as np
import uuid

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/upload/')
async def upload(file: UploadFile = File(...)):
    imgstuff.fromTmpFile(file.file)
    return {'hello': 'worls'}

    #if imgstuff.testSave(f'{name}.jpg'):
    #    return (f'http://mama.lan:1234/dl?corner={path}', 200)
    #return (f'fejl', 500)
    #return {'file_name': file.filename}

@app.get('/')
async def main():
    return {'hello': 'worls'}


'''
@app.get('/')
async def main():
    image = request.files['image']
    name = uuid.uuid4()
    image.save(f'uploads/{name}.jpg')
    if imgstuff.testSave(f'{name}.jpg'):
        return (f'http://mama.lan:1234/dl?corner={path}', 200)
    return (f'fejl', 500)


@app.route('/image/', methods=['POST'])
async def get_image():
    card = request.args.get('card')
    corner = request.args.get('corner')
    if card:
        return app.send_static_file(f'downloads/cards/{card}.jpg')
    elif corner:
        return app.send_static_file(f'downloads/corners/{corner}.jpg')
    else:
        return 'fejl', 500
'''


if __name__ == '__main__':
    uvicorn.run(app)

