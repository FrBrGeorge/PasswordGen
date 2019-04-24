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
import re
from html.parser import HTMLParser


def get_txt(url, name):
    '''Get textfile with words
    E. g. from https://github.com/first20hours/google-10000-english
    (name is unused)

    >>> len(get_txt(URLS["google-10000-english"][0],"").split())
    10000
    '''
    return urlopen(url).read().decode()


def get_tar(url, fname):
    '''Get tar[.gz|.bz2|...] file and extract data from filename
    E. g. "./usr/dict/linux.words" from "http://www.ibiblio.org/pub/Linux/libs/linux.words.2.tar.gz"

    >>> get_tar("http://www.ibiblio.org/pub/Linux/libs/linux.words.2.tar.gz","./usr/dict/linux.words").split()[-1]
    'Zurich'
    '''
    with urlopen(url) as f:
        with io.BytesIO(f.read()) as fd:
            with tarfile.open(fname, "r", fd) as v:
                with v.extractfile(fname) as w:
                    return w.read().decode()


class HTMLFilter(HTMLParser):
    '''Filter text from HTML body
>>> f=HTMLFilter()
>>> s="""<html><body><ul>
... <ul>
...   <li><a href="/licenses/gpl.html">Последняя версия GPL, версия 3</a></li>
...   <li><a href="/licenses/gpl-violation.html">Что делать, если вы видите возможное
... нарушение GPL</a></li>
...   <li><a href="/licenses/old-licenses/gpl-2.0-translations.html">Переводы
... GPLv2</a></li>
...   <li><a href="/licenses/old-licenses/gpl-2.0-faq.html">Вопросы и ответы о
... GPLv2</a></li>
... </ul></body></html>"""
>>> f.feed(s)
>>> print(f.text.strip())
Последняя версия GPL, версия 3
  Что делать, если вы видите возможное
нарушение GPL
  Переводы
GPLv2
  Вопросы и ответы о
GPLv2
    '''
    visible = False
    text = ""

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "body":
            self.visible = True

    def handle_endtag(self, tag):
        if tag.lower() == "body":
            self.visible = False

    def handle_data(self, data):
        if self.visible:
            self.text += data


def get_html(url, fname):
    '''Get html text and filter out all tags

    >>> get_html("https://www.gnu.org/licenses/old-licenses/gpl-2.0.html","").count("intended")
    4
    '''
    flt = HTMLFilter()
    flt.feed(urlopen(url).read().decode())
    return flt.text


def get(name):
    '''Get sequence of words from various sources

    >>> get("google-10000-english")[42]
    'but'
    >>> get("linux.words")[12345]
    'determined'
    >>> get("GPLv2").count("restrictions")
    3
    '''
    url, name, get, flt = URLS[name]
    return re.findall(flt, get(url, name))


def getvoc(name):
    '''Get word list and unique sort them
    >>> getvoc("google-10000-english")[-100]
    'wrapped'
    '''
    return sorted(set(get(name)))


reENG = re.compile(r"[A-Za-z]+")
reRUS = re.compile(r"[А-Яа-я]+")
reALL = re.compile(r".+")

Site = namedtuple("URLS", "URL name get filter")

URLS = {"google-10000-english": Site("https://github.com/first20hours/google-10000-english/raw/master/google-10000-english.txt", "google-10000-english", get_txt, reENG),
        "linux.words": Site("http://www.ibiblio.org/pub/Linux/libs/linux.words.2.tar.gz", "./usr/dict/linux.words", get_tar, reENG),
        "anna-karenina": Site("http://tolstoy.ru/online/online-fiction/anna-karenina/", "anna-karenina", get_html, reRUS),
        "GPLv2": Site("https://www.gnu.org/licenses/old-licenses/gpl-2.0.html", "gpl2", get_html, reENG),
        }
