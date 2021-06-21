FROM python:3

ARG mongo_uri="mongodb://localhost:27017"

ENV CDIO_MONGO_PASS=$mongo_uri

RUN apt-get update
RUN apt-get install libgl1-mesa-glx -y

RUN pip install opencv-python imutils uvicorn fastapi python-multipart scikit-image pymongo

EXPOSE 80

COPY ./project/api /api
COPY ./project/cvengine /cvengine
COPY ./project/models /models
COPY ./project/database /database

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"] 
