#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# BeautifulSoup doc list:
# http://rsj217.diandian.com/post/2012-11-01/40041235132
# http://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html#Iterating%20over%20a%20Tag
# http://www.crummy.com/software/BeautifulSoup/bs3/documentation.html

#from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup           # HTML
import re
from link_img_obj import *

class DDHTMLParser():

    def __init__(self):
        self._soup = None
        pass

    def parse_html(self, html):
        self._soup = BeautifulSoup(html)

    def list_img(self):
        return self._soup.findAll('img')

    def list_a(self):
        return self._soup.findAll('a')

    def list_a_with_img(self):
        link_imgs = []
        for a in self.list_a():
            try:
                if a['href'] and a.img and a.img['src']:
                    t = LinkImgObj()
                    t.set_href(a['href'])
                    t.set_imgsrc(a.img['src'])
                    link_imgs.append(t)
            except Exception,e:
                pass
        return link_imgs
            

