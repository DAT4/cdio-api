import os
import cv2 as cv

images = os.listdir('resources')
for i in range(len(images)):
    print(images[i])
    img = cv.imread(f'resources/{images[i]}')
    print(img)
