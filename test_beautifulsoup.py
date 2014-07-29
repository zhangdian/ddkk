#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
from BeautifulSoup import BeautifulSoup           # HTML
#from BeautifulSoup import BeautifulStoneSoup      # XML
#import BeautifulSoup                              # ALL

import re

doc = [
    '<html><head><title>Page title</title></head>',
    '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
    '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
    '</html>'
]

soup = BeautifulSoup(''.join(doc))

html = soup.html
print soup.prettify()

imglist = soup.findAll('p')
for img in imglist:
    print img


