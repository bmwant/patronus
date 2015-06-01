# -*- coding: utf-8 -*-
__author__ = 'Most Wanted'
import asyncio
import logging

from .handlers import BaseServerHandler
from .response import HttpResponse


class Patronus(object):
    def __init__(self):
        self.routes = {}

    @asyncio.coroutine
    def __call__(self, req, res):
        logging.debug('Patronus get control of it!')
        if req.route_key in self.routes:
            data = self.routes[req.route_key]()
            res.write(data)
        else:
            res.status = 404
            res.write('Page not found')

    def route(self, url, **kwargs):
        #todo: Patronus need mapper not just dictionary
        def route(f):
            self.routes[url] = f
            return f
        return route

    def run(self, host='127.0.0.1', port=9876):
        loop = asyncio.get_event_loop()
        loop.create_task(asyncio.start_server(BaseServerHandler(self),
                                              host=host, port=port, loop=loop))
        print('Running...')
        loop.run_forever()
        loop.close()

