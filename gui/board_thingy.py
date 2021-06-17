from os import listdir
from core import *

print('this is the board thingy')

images = [get(f'boards/out/{x}') for x in listdir('boards/out')]

img = images[0]

show(img)
