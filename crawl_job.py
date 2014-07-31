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

class CrawlJob():

    def __init__(self, linkobj):
        self._jobname = "crawl_job_%s" % uuid.uuid1()
        self._jobs = []
        self._jobs.append(linkobj)

    def start(self):

        while len(self._jobs) > 0:
            job = self._jobs.pop(0) # pop ele from head

            # parse url, fetch html, parse urls
            urlparser = URLParser()
            urlparser.parse(job.get_href())

            if urlparser.get_hostname():
                httpinst = Http(urlparser.get_hostname(), urlparser.get_port())
                resp = httpinst.do(urlparser.get_path(), 'GET')
                
                htmlparser = DDHTMLParser()
                htmlparser.parse_html(resp[2])

                if job.get_depth() < 3: # max depth
                    for l in htmlparser.list_links():
                        newjob = LinkObj(l, job.get_href(), job.get_depth() + 1)
                        self._jobs.append(newjob) # insert ele to tail

                for l in htmlparser.list_a_with_img():
                    '''
                    遍历每个图片链接
                    '''
                    l.set_phref = job.get_href()
                    
                    _urlparser = URLParser()
                    _urlparser.parse(l.get_imgsrc())

                    # parse img url, fetch images
                    if _urlparser.get_hostname():
                       _httpinst = Http(_urlparser.get_hostname(), _urlparser.get_port())
                       try:
                           resp = _httpinst.do(_urlparser.get_path(), 'GET')
                           _imgparser = ImageParser(resp[2])
                           if _imgparser.get_horizontal_size() >= 300 and _imgparser.get_vertical_size >= 200:
                               _imgparser.save()
                       except Exception, e:
                           pass

    


