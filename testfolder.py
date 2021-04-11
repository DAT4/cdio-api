import os
import imgstuff

if __name__ == '__main__':
    x = os.listdir('resources')
    for x in x:
        print(x)
        try:
            imgstuff.showCard(x)
        except:
            print('error')
    imgstuff.done()

