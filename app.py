import os
from flask import Flask, request, abort
from result import Result


app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return """Hello, welcome to NTU department API by ruby0322.
Please visit https://ntu-dept-code.herokuapp.com/dept_code_api for NTU Department Code API.
Please visit https://ntu-dept-code.herokuapp.com/dept_name_api for NTU Department Name API.
Please visit https://hackmd.io/@ruby0322/BJjgtcD0F for the official API Docs."""

@app.route('/dept_code_api', methods=['GET'])
def dept_code_api() -> dict:

    args = request.args

    return Result(
        **{
            'query_type': Result.QUERY_TYPE_DEPT_CODE,
            'dept_name': args['dept_name'] if 'dept_name' in args else ''
        }
    ).as_json_dict()

@app.route('/dept_name_api', methods=['GET'])
def dept_name_api() -> dict:

    args = request.args

    return Result(
        **{
            'query_type': Result.QUERY_TYPE_DEPT_NAME,
            'dept_code': args['dept_code'] if 'dept_code' in args else '',
            'name_format': args['name_format'] if 'name_format' in args else 'short'
        }
    ).as_json_dict()

if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
    app.run()
    
