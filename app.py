import os
from flask import Flask, request, abort
from config import *

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return """Hello, welcome to GAN API."""

@app.route('/gan_text', methods=['GET'])
def dept_code_api() -> dict:
    return convert(request.args.get('to_convert'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run()