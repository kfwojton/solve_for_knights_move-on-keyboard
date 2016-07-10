
info = [ ['A','B','C','D','E'],
         ['F','G','H','I','J'],
         ['K','L','M','N','O'],
         ['x','1','2','3','x']

              ]

vowels = ['A','E','I','O','U']
Vowels_Coord = [(1,1),(1,5),(2,4),(3,5)]

def alter(x,y):

    return info[x-1][y-1]

def starter(value,how_many):

    k = [b for b in info if value in b]
    k = k[0]
    position = info.index(k) , k.index(value)
    x, y = position
    xo, yo = position
    k = km((x+1,y+1),how_many-1)
    p = [o for o in k]
    s =  [''.join([alter(time[0],time[1]) for time in io]) for io in p]
    return s


def km(current, remaining):



    if remaining == 0:

        yield [current]

    else:
        x, y = current
        for move in [(x+i, y+j) for i in [2,1,-1,-2] for j in [2,1,-1,-2]
            if j != i and -j != i and x+i >= 1 and x+i <= 4 and y+j >= 1 and y+j <= 3]:
                for path in km(move, remaining-1):
                    this = [current] + path
                    if info[x-1][y-1] in vowels:
                        if len([lk for lk in this if lk in Vowels_Coord])==2:

                            print '[found a vowel]'
                            pass
                        else:
                            yield [current] + path

                    else:

                        if info[x-1][y-1] == 'x':

                            pass

                        yield [current] + path
