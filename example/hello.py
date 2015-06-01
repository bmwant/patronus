# -*- coding: utf-8 -*-
__author__ = 'Most Wanted'
from patronus import Patronus

app = Patronus()


@app.route('/')
def hello():
    return 'Hello Patronus!'

@app.route('/another')
def another():
    return 'Another route'

if __name__ == '__main__':
    app.run()