#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

# Doc list:
# https://docs.python.org/2.7/library/urlparse.html?highlight=urlparser

from urlparse import urlparse

class URLParser():

    def __init__(self):
        self._scheme = ""
        self._netloc = ""
        self._path = ""
        self._params = ""
        self._query = ""
        self._fragment = ""
        self._hostname = ""
        self._port = ""
    def parse(self, url):
        o = urlparse(url)
        if o:
            self._scheme = o.scheme
            self._netloc = o.netloc
            self._path = o.path
            self._params = o.params
            self._query = o.query
            self._fragment = o.fragment
            self._hostname = o.hostname
            self._port = o.port

    def get_scheme(self):
        return self._scheme

    def get_path(self):
        return self._path

    def get_hostname(self):
        return self._hostname

    def get_port(self):
        return self._port
