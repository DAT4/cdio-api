import numpy as np
import pickle
from pymongo import MongoClient
from bson.binary import Binary

cli = MongoClient('mongodb://mongo.lan:27017')
col = cli['cdio']['images']

def save_img(num, sym, img):
    img = Binary(pickle.dumps( img, protocol=2), subtype=128)
    res = col.insert_one({
            'number': num,
            'symbol': sym,
            'image': img,
            })
    print('Response', res.inserted_id)

def get_all():
    out = []
    res = col.find()
    for x in res:
        x['image'] = pickle.loads(x['image'])
        out.append(x)
    return out

