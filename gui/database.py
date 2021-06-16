import numpy as np
import pickle
from pymongo import MongoClient
from bson.binary import Binary

cli = MongoClient('mongodb://mama.sh:27019')
COL_SYM = cli['cdio']['symbols']
COL_NUM = cli['cdio']['numbers']

def save_symbol(sym, name):
    sym = Binary(pickle.dumps( sym, protocol=2), subtype=128)
    res = COL_SYM.insert_one({
            'symbol': sym,
            'name': name,
            })
    print('Response', res.inserted_id)

def save_number(num, name):
    num = Binary(pickle.dumps( num, protocol=2), subtype=128)
    res = COL_NUM.insert_one({
            'number': num,
            'name': name,
            })
    print('Response', res.inserted_id)


def get_all_nums():
    out = []
    res_num = COL_NUM.find()
    for x in res_num:
        x['number'] = pickle.loads(x['number'])
        out.append(x)
    return out

def get_all_syms():
    out = []
    res_sym = COL_SYM.find()
    for x in res_sym:
        x['symbol'] = pickle.loads(x['symbol'])
        out.append(x)
    return out