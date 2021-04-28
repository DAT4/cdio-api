from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

from .imgstf import edge as im

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
    img = im.save(im.load(file.file))
    return StreamingResponse(img, media_type='image/jpg')
