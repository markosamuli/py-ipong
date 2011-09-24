#!/usr/bin/env python

import argparse
import re

from gevent import wsgi
from gevent import monkey

monkey.patch_all()

# from gevent.pool import Pool

def application(env, start_response):
    
    if env['PATH_INFO'] == '/favicon.ico':
        start_response('204 No Content', [])
        return ['']
    
    if env['PATH_INFO'] == '/':
        if 'HTTP_X_REAL_IP' in env:
            output = env['HTTP_X_REAL_IP']
        else:
            output = env['REMOTE_ADDR']
        start_response('200 OK', [('Content-type', 'text/plain')])
        return [output]
        
    start_response('404 Not Found', [('Content-type', 'text/plain')])
    return ['Ping pong!']
    
def valid_address(string):
    if re.match('^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$', string):
        return string    
    msg = "%s is not valid address" % string
    raise argparse.ArgumentTypeError(msg)
    
def main():
    parser = argparse.ArgumentParser(description='ipong server')
    parser.add_argument('--address', type=valid_address, default='127.0.0.1')    
    parser.add_argument('--port', type=int, default=8088)
    args = parser.parse_args()
    address = args.address
    port = args.port
    print "ipong -- starting server at http://" + address + ":" + str(port)
    #pool = Pool(10000) # do not accept more than 10000 connections
    #pywsgi.WSGIServer((host, port), application, spawn=pool).serve_forever()
    wsgi.WSGIServer((address, port), application).serve_forever()

if __name__ == '__main__':
    main()