from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .imgstf import edge as im
from .database import database as db

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db          = db.Database('mongodb://mama.sh:27019')
img_machine = im.ImageMachine(db)

@app.post('/upload/')
async def upload(file: UploadFile = File(...)):
    img = im.save(im.load(file.file))
    return StreamingResponse(img, media_type='image/jpg')

@app.post('/board/')
async def upload(file: UploadFile = File(...)):
    return JSONResponse(content=img_machine.gamestate_from_board(file.file))
