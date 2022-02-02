from os import stat
from flask import Flask, request, abort
from result import Result


app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'hello, world!'

@app.route('/api', methods=['GET'])
def api() -> str:

    args = request.args

    if 'dept_name' in args:
        dept_name = args['dept_name']
        print(dept_name)
    else:
        dept_name = ''
        print('Dept name missing.')

    return Result(dept_name).as_json_dict().__repr__()

if __name__ == '__main__':
    app.run()
    
