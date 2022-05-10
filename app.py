import os
from flask import Flask, request, abort, render_template
from config import *

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return """Hello, welcome to GAN API."""

@app.route('/gan_text', methods=['GET'])
def gan_text_api() -> str:
    return {
        'converted': convert(request.args.get("to_convert"))
    }

@app.route('/gan', methods=['GET'])
def gan_gui():
    return render_template('gan_wen_api.html')

@app.route('/examples', methods=['GET'])
def examples():
    return render_template('examples.html')

@app.route('/tutorial', methods=['GET'])
def tutorial():
    return render_template('tutorial.html')

@app.route('/rand_wiki', methods=['GET'])
def rand_wiki_api():
    return random_wiki()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)