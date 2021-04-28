from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

import uvicorn, imgstuff

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
    img = imgstuff.save(imgstuff.load(file.file))
    return StreamingResponse(img, media_type='image/jpg')


if __name__ == '__main__':
    uvicorn.run(app)

