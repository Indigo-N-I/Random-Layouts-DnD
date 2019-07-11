import random as rand

def getRoom(squreMeters):
    x = rand.randint(5, int(squreMeters/5))
    y = int(squreMeters/x)
    return x,y

def round(number):
    return int(number) if number-int(number) < .5 else int(number) + 1

def getEnterence(size):
    x = rand.randint(1,size)
    y = round(size/x)
    return x,y

def create(lower, upper):
    area = rand.randint(lower, upper)
    x, y = getRoom(area)
    left = int(area  - x*y) if area - x*y > 0 else 0
    #print('The number of tiles left is:', left)
    if left > 0:
        enterx, entery = getEnterence(left)
    else:
        enterx, entery = 0,0
    return x, y, enterx, entery

def getDimentions(size):
    if size == 'S': #small means you get 2000 - 3000 square feet
                    #80-120 5by5 squares
        return create(80-120)
    if size == 'M': #5000-7000 square feet
                    #200-280 5x5 squares
        return create(200-280)
    if size == 'L': #10000-15000 square feet
                    #400- 600 5x5 tiles
        return create(400-600)
