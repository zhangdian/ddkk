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

    def __init__(self, linkobj):
        self._jobname = "crawl_job_%s" % uuid.uuid1()
        self._linkobj = linkobj

    def start(self):
        # parse url, fetch html, parse urls
        urlparser = URLParser()
        urlparser.parse(self._linkobj.get_href())

        if urlparser.get_hostname():
            httpinst = Http(urlparser.get_hostname(), urlparser.get_port())
            resp = httpinst.do(urlparser.get_path(), 'GET')
            
            htmlparser = DDHTMLParser()
            htmlparser.parse_html(resp[2])

            links = htmlparser.list_links()
            for l in links:
                # TODO: 添加新的任务 LinkObj
                pass

            imglinkobjs = htmlparser.list_a_with_img()
            for l in imglinkobjs:
                '''
                遍历每个图片链接
                '''
                l.set_phref = self._linkobj.get_href()
                
                _urlparser = URLParser()
                _urlparser.parse(l.get_imgsrc())

                # parse img url, fetch images
                if _urlparser.get_hostname():
                   _httpinst = Http(_urlparser.get_hostname(), _urlparser.get_port())
                   resp = _httpinst.do(_urlparser.get_path(), 'GET')
                   try:
                       _imgparser = ImageParser(resp[2])
                       if _imgparser.get_horizontal_size() >= 400 and _imgparser.get_vertical_size >= 200:
                           _imgparser.save()
                   except Exception, e:
                       pass

    


