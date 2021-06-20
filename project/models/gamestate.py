from cvengine import edge as im

class GameState:
    def __init__(self, db, board_image):
        self.nums = db.get_numbers()
        self.syms = db.get_symbols()
        self.__gamestate_from_board(board_image)

    def __gamestate_from_board(self, board_image):
        cards = [im.get_card(x)
                for x
                in self.split_board(board_image)]

        for card in cards:
            card.find_values(self.nums, self.syms)

        self.builds = cards[:7]
        self.suits  = cards[-4:]
        self.deck   = cards[-5]

    def split_board(self, img):
        def is_card_pos(i,j): return i!=1 or j!=1 and j!=2
        h,w,_ = img.shape
        w, h, = w//7, h//2
        return [img[i*h:i*h+h,j*w:j*w+w]
                for i in range(2)
                for j in range(7)
                if is_card_pos(i,j)]


    def json(self):
        return {
                'builds': [str(x) for x in self.builds],
                'suits': [str(x) for x in self.suits],
                'deck': str(self.deck),
                }
