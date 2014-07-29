#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

import uuid
from http import *
from htmlparser import *
from HTMLParser import *
from link_img_obj import *
from urlparser import *
from imageparser import *

class CrawlJob():

    def __init__(self, linkdepth, url):
        self._jobname = "crawl_job_%s" % uuid.uuid1()
        self._linkdepth = linkdepth + 1
        self._url = url

    def exec(self):
        links = [] # all links to analyze

        # parse url, fetch html, parse urls
        parser = URLParser()
        parser.parse(url)

        if parser.get_hostname():
            httpinst = Http(parser.get_hostname(), parser.get_port())
            # TODO


        # parse img url, fetch images
        if parser.get_hostname():
           httpinst = Http(parser.get_hostname(), parser.get_port())
           resp = httpinst.do(parser.get_path(). 'GET')
           try:
               imgparser = ImageParser(resp[2])
               if imgparser.get_horizontal_size() >= 400 and imgparser.get_vertical_size >= 200:
                   imgparser.save()
            except Exception, e:
                pass

    


