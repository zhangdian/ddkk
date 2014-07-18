#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

from http import *
from htmlparser import *
from HTMLParser import *

inst = Http("www.sohu.com", 80)
resp = inst.do("/", "GET")
print resp[0]
print resp[1]

data = resp[2]

# http://rsj217.diandian.com/post/2012-11-01/40041235132
# 决定用BeautifulSoup 


parser = DDHTMLParser()
try:
    parser.feed(data)
except HTMLParser.HTMLParseError,e:
    print e

