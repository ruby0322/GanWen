import os
import re
from flask import Flask, request, abort, render_template, redirect
from config import *

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect('https://ganwenapi.herokuapp.com/gan')

@app.route('/gan_text', methods=['GET'])
def gan_text_api():
    return {
        'converted': convert(request.args.get("to_convert"))
    }

@app.route('/bs', methods=['GET'])
def bullshit():
    return {
        'bullshit': get_bs(request.args.get('topic'), request.args.get('len'))
    }

@app.route('/gan', methods=['GET'])
def gan_gui():
    return render_template('gan.html')

@app.route('/tutorial', methods=['GET'])
def tutorial():
    return render_template('tutorial.html')

@app.route('/rand_wiki', methods=['GET'])
def rand_wiki_api():
    return random_wiki()

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/api', methods=['GET'])
def api():
    return render_template('api.html')

@app.route('/what', methods=['GET'])
def what():
    return render_template('what.html')



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)