#!/usr/bin/env python

import sys
import os

# append project to the path
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root)

from gevent import wsgi
from ipong import application

def main():
    wsgi.WSGIServer(('', 8088), application).serve_forever()
    print sys.path
#path = os.path.join(dirname(dirname(__file__)))
#print path
# sys.path.append()

if __name__ == '__main__':
    main()