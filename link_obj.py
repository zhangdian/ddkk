#! /usr/bin/env python
# -*- coding: utf-8 -*-
#


class LinkObj():

    def __init__(self, href, phref, depth):
        self._href = href
        self._phref = phref
        self._depth = depth
        pass

    def set_href(self, href):
        self._href = href

    def get_href(self):
        return self._href

    def ser_phref(self, phref):
        self._phref = phref

    def get_phref(self):
        return self._phref

    def get_depth(self):
        return self._depth

    def set_depth(self, depth):
        self._depth = depth
