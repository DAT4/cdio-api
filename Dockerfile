FROM python:3

RUN apt-get update
RUN apt-get install libgl1-mesa-glx -y

RUN pip install opencv-python imutils uvicorn fastapi python-multipart scikit-image

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"] 
