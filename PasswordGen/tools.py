#!/usr/bin/env python3
'''
Some common tools

>>> [f"{a}{c:.3}" for f in EN for a,c in f.items()]
['0.167', 'A0.167', 'O0.167', 'U0.167', 'I0.167', 'E0.167', '0.0455', 'B0.0455', 'C0.0455', 'D0.0455', 'F0.0455', 'G0.0455', 'H0.0455', 'J0.0455', 'K0.0455', 'L0.0455', 'M0.0455', 'N0.0455', 'P0.0455', 'Q0.0455', 'R0.0455', 'S0.0455', 'T0.0455', 'V0.0455', 'W0.0455', 'X0.0455', 'Y0.0455', 'Z0.0455']
'''
# runargs: -i

def createvoc(chars):
    '''Create {char:probability} dicte from chars
    with uniform probability, all theese includes "" added to characters
    '''
    return dict(zip(("",)+tuple(chars),(1/(len(chars)+1),)*(len(chars)+1)))

def pair(r):
    '''Convert a number, or a range, or a pair into pair:
    >>> pair((1,2))
    (1, 2)
    >>> pair(range(1,2))
    (1, 2)
    >>> pair(1)
    (1, 2)
    '''
    try:
        return r[0], r[1]
    except:
        try:
            return r.start, r.stop
        except:
            return r, r+1

RU = createvoc("АОУЫЭЯЁЮИЕ"), createvoc("БВГДЖЗЙКЛМНПРСТФХЦЧШЩ")
EN = createvoc("AOUIE"), createvoc("BCDFGHJKLMNPQRSTVWXYZ")

