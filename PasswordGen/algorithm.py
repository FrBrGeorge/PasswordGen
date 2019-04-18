#!/usr/bin/env python3
'''
Password/passhprase generation algorithms
'''

import random
from itertools import chain, zip_longest

def passphrase(words, seps, nwords, wboundary=None, seed=None):
    '''Generate passphrase from nwords of words when word len in nboundaryi
    >>> len(passphrase("1234567890","+-*/", 8))
    15
    >>> passphrase("A","b", 8)
    'AbAbAbAbAbAbAbA'
    >>> r=passphrase("AB","cd", 8)
    >>> r.count("A")+r.count("B"), r.count("c")+r.count("d")
    (8, 7)
    >>> sorted(set("".join(passphrase(("xot", "toxx", "tooxoo", "ooxoot"), "/", range(2,5)).split("/"))))
    ['o', 't', 'x']
    >>> set(passphrase("A","b", 18)[::2]).pop()
    'A'
    >>> set(passphrase("A","b", 18)[1::2]).pop()
    'b'
    '''
    if seed:
        random.seed(seed)
    if type(nwords) is range:
        nwords = random.randrange(nwords.start, nwords.stop)
    if not hasattr(words, "__mul__"):
        words = tuple(words)
    if not hasattr(seps, "__mul__"):
        seps = tuple(seps)
    seps *= 1+(nwords-1)//len(seps)
    words *= 1+nwords//len(words)
    s = random.sample(seps, nwords-1)
    w = random.sample(words, nwords)
    ret = "".join(chain(*zip_longest(w, s, fillvalue="")))
    return ret

