from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from cvengine import edge as im
from database.mongo import MongoDB
from models.gamestate import GameState

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db          = MongoDB('mongodb://mama.sh:27019')
img_machine = im.ImageMachine(db)

@app.post('/upload/')
async def upload(file: UploadFile = File(...)):
    img = im.save(im.load(file.file))
    return StreamingResponse(img, media_type='image/jpg')

@app.post('/board/')
async def upload(file: UploadFile = File(...)):
    gamestate = GameState(db, im.load(file.file))
    return JSONResponse(content=gamestate.json())
