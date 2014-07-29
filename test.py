#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

from http import *
from htmlparser import *
from HTMLParser import *
from link_img_obj import *

inst = Http("news.163.com", 80)
resp = inst.do("/", "GET")
print resp[0]
print resp[1]

data = resp[2]

# http://rsj217.diandian.com/post/2012-11-01/40041235132
# 决定用BeautifulSoup 

parser = DDHTMLParser()
parser.parse_html(data)

l = parser.list_a_with_img()

for a in l:
    print a.get_href()
    print a.get_imgsrc()

