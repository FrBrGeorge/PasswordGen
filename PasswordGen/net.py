#!/usr/bin/env python3
'''
Get a word dictionary from various sources

Now supports only https://github.com/first20hours/google-10000-english

>>> type(Site.URL)
<class 'property'>
>>> type(Site.get)
<class 'property'>
>>> URLS["google-10000-english"].URL.split('/')[3]
'first20hours'
>>> len(URLS)>=1
True

'''
# python3 -c 'import urllib.request; import random; print(" ".join(random.sample(urllib.request.urlopen("https://github.com/first20hours/google-10000-english/raw/master/google-10000-english.txt").read().decode().split(),4)))'
#
# TODO linux words http://www.ibiblio.org/pub/Linux/libs/linux.words.2.tar.gz

from urllib.request import urlopen
from collections import namedtuple

def get_txt(name):
    '''Get textfile with words
    E. g. from https://github.com/first20hours/google-10000-english

    >>> len(get_txt("google-10000-english"))
    10000
    '''
    return urlopen(URLS[name].URL).read().decode().split()

Site = namedtuple("URLS", "URL get")

URLS = { "google-10000-english": Site("https://github.com/first20hours/google-10000-english/raw/master/google-10000-english.txt", get_txt) }
