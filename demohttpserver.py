#!/usr/bin/env python3

import sys
from flask import stream_with_context, request, Response
from flask import Flask

app = Flask("demo-http-server")

CHUNK_SIZE = 65536
CHUNK = 'a' * CHUNK_SIZE

@app.route('/demo/<size>')
def supply(size):
    def generate(size):
        size = int(size)
        rnd = int(size / CHUNK_SIZE)
        for i in range(rnd):
            print('percentage: {:.2%}'.format(i * CHUNK_SIZE / size))
            yield CHUNK
        yield 'a' * (size - rnd * CHUNK_SIZE)
        print('percentage: {:.2%}'.format(1))

    response = Response(generate(size), mimetype='text/txt')
    response.headers['content-length'] = size
    return response


if __name__ == '__main__':
    host = '127.0.0.1' if len(sys.argv) < 2 else sys.argv[1]
    port = 6666 if len(sys.argv) < 3 else int(sys.argv[2])
    CHUNK_SIZE = CHUNK_SIZE if len(sys.argv) < 4 else int(sys.argv[3])
    CHUNK = 'a' * CHUNK_SIZE
    app.run(host=host, port=port)
