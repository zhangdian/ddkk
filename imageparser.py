#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Doc list
# http://onlypython.group.iteye.com/group/wiki/1371-python-graphics-library-pil-python-image-library-introduction

from PIL import Image
import StringIO
import time
import uuid

IMG_PATH = "/opt/images/"

class ImageParser():

    def __init__(self, data):
        self._data = data
        self._img = Image.open(StringIO.StringIO(data))
        self._path = "%s_%s" % (str(time.time()), uuid.uuid1())

    def save(self):
        try :
            f = open("%s%s" % (IMG_PATH, self._path), 'w')
            f.write(self._data)
            f.flush()
            f.close()
        except Exception,e :
            pass

    def get_size(self):
        '''
        return (100, 100)
        '''
        return self._img.size

    def get_vertical_size(self):
        return self._img.size[1]

    def get_horizontal_size(self):
        return self._img.size[0]

    def get_filename(self):
        return self._path
