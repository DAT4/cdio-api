from cvengine import edge as im

class GameState:
    def __init__(self, db, cards):
        self.nums = db.get_numbers()
        self.syms = db.get_symbols()
        self.__gamestate_from_board(board_image)

        for card in cards:
            card.find_values(self.nums, self.syms)

        self.builds = cards[:7]
        self.suits  = cards[-4:]
        self.deck   = cards[-5]

    def json(self):
        return {
                'builds': [str(x) for x in self.builds],
                'suits': [str(x) for x in self.suits],
                'deck': str(self.deck),
                }
