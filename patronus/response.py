# -*- coding: utf-8 -*-
__author__ = 'Most Wanted'
from contextlib import closing
from http.server import BaseHTTPRequestHandler

STATUSES = BaseHTTPRequestHandler.responses


class HttpResponse(object):
    """
    Silly basic http response for testing
    """
    def __init__(self, writer, status=200, content_type='text/html'):
        self.status = int(status)
        self.writer = writer
        self.headers = [
            'Content-Encoding: utf-8',
            'Content-Type: %s' % content_type,
        ]

    def write(self, data):
        # Status line first
        self.writer.write('HTTP/1.1 {status} {status_message}\r\n'.format(status=self.status,
            status_message=STATUSES[self.status][0]).encode('utf-8'))

        for header in self.headers:
            self.writer.write(header.encode())  # utf-8 by default
            self.writer.write('\r\n'.encode())
        self.writer.write('\r\n'.encode())

        with closing(self.writer):
            if isinstance(data, str):
                data = data.encode()

            if isinstance(data, bytes):
                self.writer.write(data)
                self.writer.write_eof()
            else:
                raise ValueError('Data must be bytes instance. Get %s instead' % type(data))
