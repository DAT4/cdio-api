from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, JSONResponse
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

@app.post('/board/')
async def upload(file: UploadFile = File(...)):
    game_state = {
            'builds':['H2', 'S8', 'S0', 'D13', 'K4', 'D8', 'K10',],
            'suits':['H0', 'D4', '', '',],
            'deck':'K11',
            }
    return JSONResponse(content=game_state)
