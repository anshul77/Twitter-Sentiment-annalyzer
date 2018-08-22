# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 11:20:24 2018

@author: anshul
"""

import bs4 as bs
import urllib.request

# Gettings the data source
source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Global_warming').read()

# Parsing the data/ creating BeautifulSoup object
soup = bs.BeautifulSoup(source,'lxml')