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
# runargs: -i

from urllib.request import urlopen
from collections import namedtuple
import tarfile
import io

def get_txt(url, name):
    '''Get textfile with words
    E. g. from https://github.com/first20hours/google-10000-english
    (name is unused)

    >>> len(get_txt(URLS["google-10000-english"][0],""))
    10000
    '''
    return urlopen(url).read().decode().split()

def get_tar(url, fname):
    '''Get tar[.gz|.bz2|...] file and extract data from filename
    E. g. "./usr/dict/linux.words" from "http://www.ibiblio.org/pub/Linux/libs/linux.words.2.tar.gz"

    >>> get_tar("http://www.ibiblio.org/pub/Linux/libs/linux.words.2.tar.gz","./usr/dict/linux.words")[-1]
    'Zurich'
    '''
    with urlopen(url) as f:
        with io.BytesIO(f.read()) as fd:
            with tarfile.open(fname, "r", fd) as v:
                with v.extractfile(fname) as w:
                    return w.read().decode().split()

def get(name):
    '''Get sequence of words from various sources

    >>> get("google-10000-english")[42]
    'but'
    >>> get("linux.words")[12345]
    'determiner'
    '''
    url, name, get = URLS[name]
    return get(url, name)

Site = namedtuple("URLS", "URL name get")

URLS = { "google-10000-english": Site("https://github.com/first20hours/google-10000-english/raw/master/google-10000-english.txt", "google-10000-english", get_txt),
         "linux.words": Site("http://www.ibiblio.org/pub/Linux/libs/linux.words.2.tar.gz", "./usr/dict/linux.words", get_tar),
       }
