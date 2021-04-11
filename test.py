import requests
import cv2 as cv

url = 'http://localhost:1234/'

def useWebCam():
    cap = cv.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    cap.set(10,100)

    while True:
        success, img = cap.read()
        findCard(img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

with open('ace.jpg', 'rb') as f:
    image = f.read()

files= {
        'image': (
            'image.jpg',
            image,
            'multipart/form-data',
        )
    }

r = requests.post(url, files=files)
print(r)
