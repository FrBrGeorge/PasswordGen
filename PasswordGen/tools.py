#!/usr/bin/env python3
'''
Some common tools
>>> print(*EN)
:0.167 A:0.167 O:0.167 U:0.167 I:0.167 E:0.167 :0.045 B:0.045 C:0.045 D:0.045 F:0.045 G:0.045 H:0.045 J:0.045 K:0.045 L:0.045 M:0.045 N:0.045 P:0.045 Q:0.045 R:0.045 S:0.045 T:0.045 V:0.045 W:0.045 X:0.045 Y:0.045 Z:0.045
'''
# runargs: -i

import random

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

class Voc:
    def __init__(self, chars, probs=[], empty=True):
        '''Create {char[i]:probs[i]} dict from chars
        with uniform probability by default,
        edding empty char "" as element
        if probs if defined, it must have length of chars (or +1 if empty included)
        probabilities are normalized against sum(probs)
        >>> print(Voc("1234567890"))
        :0.091 1:0.091 2:0.091 3:0.091 4:0.091 5:0.091 6:0.091 7:0.091 8:0.091 9:0.091 0:0.091
        >>> print(Voc("ABCD",empty=False))
        A:0.250 B:0.250 C:0.250 D:0.250
        >>> print(Voc("+-*",(1,2,3),empty=False))
        +:0.167 -:0.333 *:0.500
        >>> print(*(EN[0][i/7] for i in range(7)))
          A O U I E
        '''
        if empty:
            chars = ("",)+tuple(chars)
        if not probs:
            probs = (1/len(chars),)*len(chars)
        else:
            s = sum(probs)
            probs = tuple(p/s for p in probs)
        self.vocabulary = dict(zip(chars, probs))

    def __str__(self):
        return " ".join(f"{k}:{v:5.3f}" for k,v in self.vocabulary.items())

    def __getitem__(self, idx):
        if type(idx) is float:
            s = 0
            for k, v in self.vocabulary.items():
                s += v
                if s>=idx: break
            return k


RU = Voc("АОУЫЭЯЁЮИЕ"), Voc("БВГДЖЗЙКЛМНПРСТФХЦЧШЩ")
EN = Voc("AOUIE"), Voc("BCDFGHJKLMNPQRSTVWXYZ")
