#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

from HTMLParser import HTMLParser

class DDHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self._flag = False
        self._data = ""

    def handle_starttag(self, tag, attrs):
        if 'a' == tag:
            self._flag = True
        elif 'img' == tag and self._flag == True:
            self._data = self.get_starttag_text()
    def handle_endtag(self, tag):
        if 'a' == tag and self._flag == True:
            print self._data
            self._data = ""
            self._flag = False
    def handle_data(self, data):
        pass

