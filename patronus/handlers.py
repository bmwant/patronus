# -*- coding: utf-8 -*-
__author__ = 'Most Wanted'
import asyncio
import logging

from .request import HttpRequest
from .response import HttpResponse


class BaseServerHandler(object):
    def __init__(self, handler=None):
        self.handler = handler

    def __call__(self, reader, writer):
        request = HttpRequest(reader)
        if (yield from request.parse()) is False:
            logging.error('What the hell?')
            writer.close()
            return

        response = HttpResponse(writer)

        if self.handler:
            yield from self.handler(request, response)
        else:
            response.write('Patronus is called')