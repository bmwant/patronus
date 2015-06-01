# -*- coding: utf-8 -*-
__author__ = 'Most Wanted'
import asyncio


class HttpRequest(object):
    """
    Parse requests and set needed attributes to an instance
    """
    def __init__(self, reader=None):
        self.reader = reader

    @asyncio.coroutine
    def parse(self):
        req_line = (yield from self.reader.readline()).decode()

        if not req_line:
            return False

        print('type req_line', type(req_line))
        try:
            method, path, proto = req_line.split()
        except Exception as e:
            print(e)
            print('and req_line is [%s]' % req_line, type(req_line))
            raise e
        print(method, path, proto)
        self.route_key = path
        self.reader.feed_eof()

    @asyncio.coroutine
    def text(self):
        pass

    @asyncio.coroutine
    def json(self):
        pass