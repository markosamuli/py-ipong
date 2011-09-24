def application(env, start_response):
    
    if env['PATH_INFO'] == '/favicon.ico':
        start_response('204 No Content', [])
        return ['']
    
    if env['PATH_INFO'] == '/':
        output = env['REMOTE_ADDR']
        start_response('200 OK', [('Content-type', 'text/plain'), ('Content-length', str(len(output)))])
        return [output]
        
    start_response('404 Not Found', [('Content-type', 'text/plain')])
    return ['Ping pong!']
    