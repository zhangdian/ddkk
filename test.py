#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

from http import *
from htmlparser import *
from HTMLParser import *
from link_img_obj import *
from urlparser import *
from imageparser import *

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
    img_src = a.get_imgsrc()
    parser = URLParser()
    parser.parse(img_src)

    if parser.get_hostname:
        inst = Http(parser.get_hostname(), parser.get_port())
        resp = inst.do(parser.get_path(), "GET")

        try:
            imgparser = ImageParser(resp[2])
            if imgparser.get_horizontal_size() >= 400 and imgparser.get_vertical_size() >= 200:
                imgparser.save()
                print "%s, %s, %s" % (imgparser.get_filename(), imgparser.get_horizontal_size(), imgparser.get_vertical_size())
        except Exception,e:
            pass
        

