from cv2 import bitwise_xor
from os import environ as env, listdir as ls
from database.mongo import MongoDB
from cvengine import edge as im, core as co

#uri     = env['CDIO_MONGO_PASS']
#db      = MongoDB(uri)
#numbers = db.get_symbols()
#a = numbers[10].img
#b = numbers[7].img

img = im.get(f'resources/newimgs/{ls("resources/newimgs")[0]}')
im.show(co.find_card(img))
