import json
from unicodedata import name




class Result:

    OK_MESSAGE = '[OK] Department code/name found successfully.'
    NOT_FOUND_MESSAGE = '[NOT FOUND] Cannot find the corresponding department code/name.'
    EMPTY_QUERY_MESSAGE = '[NOT FOUND] An empty query string is provided.'
    ERROR_MESSAGE = '[ERROR] Some unknown error occurred during the process'

    STATUS_CODE = {}
    DEPT_CODE = {}

    QUERY_TYPE_DEPT_CODE = 0
    QUERY_TYPE_DEPT_NAME = 1

    inited = False

    def __init__(self, dept_name: str='', dept_code: str='', query_type: str='', name_format: str='') -> None:

        if not Result.inited:
            Result.init()

        try:
            if query_type == Result.QUERY_TYPE_DEPT_CODE:
                self.result = self.find_dept_code(dept_name=dept_name)
                self.query_type = 'dept_code'
                self.query_string = dept_name
            elif query_type == Result.QUERY_TYPE_DEPT_NAME:
                self.result = self.find_dept_name(dept_code=dept_code, name_format=name_format)
                self.query_type = 'dept_name'
                self.query_string = dept_code
            else:
                self.query_type = ''
                self.query_string = ''
                raise Exception()

            if self.result:
                self.status_code = Result.STATUS_CODE['OK']
                self.message = Result.OK_MESSAGE
            else:
                self.status_code = Result.STATUS_CODE['NOT_FOUND']
                self.message = Result.NOT_FOUND_MESSAGE if dept_name else Result.EMPTY_QUERY_MESSAGE
        except:
            self.result = ''
            self.status_code = Result.STATUS_CODE['ERROR']
            self.message = Result.ERROR_MESSAGE

    def find_dept_name(self, dept_code: str, name_format: str) -> str:
        if dept_code in Result.DEPT_CODE:
            index = 0
            if name_format == 'full':
                index = 0
            elif name_format == 'short':
                index = 1
            return Result.DEPT_CODE[dept_code][index]

        return ''

    def find_dept_code(self, dept_name: str) -> str:

        for key, names in Result.DEPT_CODE.items():
            if dept_name in names:
                return key

        return ''

    def as_json_dict(self) -> dict:
        return {
            'status_code': self.status_code,
            'query_type': self.query_type,
            'query_string': self.query_string,
            'result': self.result,
            'message': self.message,
        }

    @staticmethod
    def init() -> None:

        with open('status_code.json', 'r') as json_f:
            Result.STATUS_CODE = json.load(json_f)

        with open('dept_code.json', 'r', encoding='utf-8') as json_f:
            Result.DEPT_CODE = json.load(json_f)

        Result.inited = True



      


