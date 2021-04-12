import os
import imgstuff

if __name__ == '__main__':
    x = os.listdir('resources')
    for x in x:
        print(x)
        try:
            imgstuff.showCard(f'resources/{x}')
        except:
            print('error')
    imgstuff.done()

