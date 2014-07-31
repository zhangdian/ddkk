#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import httplib

class Http:

    def __init__(self, host, port):
        self._host = host
        self._port = port

    def do(self, path, method):
        conn = httplib.HTTPConnection(self._host, self._port)
        # conn.set_debuglevel(3)

        resp = None
        try:
            conn.request(method, path)
            resp = conn.getresponse()
        except Exception,e :
            pass
        if resp is not None:
            self._status = resp.status
            self._reason = resp.reason
            self._data = resp.read()
        return [self._status, self._reason, self._data]
