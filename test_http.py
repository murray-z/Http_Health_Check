# -*- coding: utf-8 -*-

import json
from flask import request, Flask
import argparse

app = Flask(__name__)


@app.route('/', methods=['POST'])
def test_server():
    data = json.loads(request.data)
    return json.dumps(data, ensure_ascii=False)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--host', default='0.0.0.0', help='host')
    args.add_argument('--port', default=9007, help='port')

    args = args.parse_args()

    host = args.host
    port = args.port

    app.run(host=host, port=port)




