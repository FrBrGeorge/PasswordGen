#!/usr/bin/env python3
'''
Some common tools

>>> [f"{a}{c:.3}" for f in EN for a,c in f.items()]
['0.167', 'A0.167', 'O0.167', 'U0.167', 'I0.167', 'E0.167', '0.0455', 'B0.0455', 'C0.0455', 'D0.0455', 'F0.0455', 'G0.0455', 'H0.0455', 'J0.0455', 'K0.0455', 'L0.0455', 'M0.0455', 'N0.0455', 'P0.0455', 'Q0.0455', 'R0.0455', 'S0.0455', 'T0.0455', 'V0.0455', 'W0.0455', 'X0.0455', 'Y0.0455', 'Z0.0455', '0.333', 'Y0.333', 'J0.333', '1.0']
'''
# runargs: -i

RU_4 = "АОУЫЭЯЁЮИЕ", "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ", "", "Ь",  
EN_4 = "AOUIE", "BCDFGHJKLMNPQRSTVWXYZ", "YJ", "",

def createvoc(vowels, consonants, vowsuff, consuff):
    '''Create 4 dicts — vowels, consonants, vowel suffixes, consonant suffixes
    with uniform probability, all theese includes "" added to characters
    >>> str(createvoc("QWE","RTYU","1",""))
    "({'': 0.25, 'Q': 0.25, 'W': 0.25, 'E': 0.25}, {'': 0.2, 'R': 0.2, 'T': 0.2, 'Y': 0.2, 'U': 0.2}, {'': 0.5, '1': 0.5}, {'': 1.0})"
    '''
    def uni(chars):
        return dict(zip(("",)+tuple(chars),(1/(len(chars)+1),)*(len(chars)+1)))
    return(uni(vowels), uni(consonants), uni(vowsuff), uni(consuff))

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

RU = createvoc(*RU_4)
EN = createvoc(*EN_4)

