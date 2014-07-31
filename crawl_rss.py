#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

import uuid
from http import *
from htmlparser import *
from HTMLParser import *
from link_img_obj import *
from link_obj import *
from urlparser import *
from imageparser import *

class CrawlRSS():

    def __init__(self, listrss):
        self._jobname = "crawl_rss_%s" % uuid.uuid1()
        self._listrss = listrss

    def start():

        pass

