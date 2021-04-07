import requests
import cv2 as cv

url = 'http://localhost:1234/'

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
