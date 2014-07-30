#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

class LinkImgObj():

    def __init__(self):
        self._href = ""
        self._imgsrc = ""
        self._phref = ""
        pass

    def set_href(self, href):
        self._href = href

    def get_href(self):
        return self._href

    def set_imgsrc(self, imgsrc):
        self._imgsrc = imgsrc

    def get_imgsrc(self):
        return self._imgsrc

    def set_phref(self, phref):
        self._phref = phref

    def get_phref(self):
        return self._phref
