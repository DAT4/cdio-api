import json
from cvengine import edge as im
from os import environ as env
from database.mongo import MongoDB
from models.gamestate import GameState

uri     = env['CDIO_MONGO_PASS']
db      = MongoDB(uri)
board   = im.get('resources/board.jpg')


gamestate = GameState(db, board)

jsonn = gamestate.json()

print(json.dumps(jsonn, indent=2))
