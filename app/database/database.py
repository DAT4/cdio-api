import numpy as np
import pickle
from pymongo import MongoClient
from bson.binary import Binary

class Database:
    def __init__(self, uri):
        cli = MongoClient(uri)
        self.COL_SYM = cli['cdio']['symbols']
        self.COL_NUM = cli['cdio']['numbers']

    def save_symbol(self, sym, name):
        sym = Binary(pickle.dumps( sym, protocol=2), subtype=128)
        res = self.COL_SYM.insert_one({
                'symbol': sym,
                'name': name,
                })
        print('Response', res.inserted_id)

    def save_number(self, num, name):
        num = Binary(pickle.dumps( num, protocol=2), subtype=128)
        res = self.COL_NUM.insert_one({
                'number': num,
                'name': name,
                })
        print('Response', res.inserted_id)


    def get_all_nums(self):
        out = []
        res_num = self.COL_NUM.find()
        for x in res_num:
            x['number'] = pickle.loads(x['number'])
            out.append(x)
        return out

    def get_all_syms(self):
        out = []
        res_sym = self.COL_SYM.find()
        for x in res_sym:
            x['symbol'] = pickle.loads(x['symbol'])
            out.append(x)
        return out
