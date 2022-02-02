import json




class Result:

    OK_MESSAGE = '[OK] Department code found successfully.'
    NOT_FOUND_MESSAGE = '[NOT FOUND] Cannot find the corresponding department code.'
    EMPTY_QUERY_MESSAGE = '[NOT FOUND] An empty query string is provided.'
    ERROR_MESSAGE = '[ERROR] Some unknown error occurred during the process'

    STATUS_CODE = {}
    DEPT_CODE = {}

    inited = False

    def __init__(self, dept_name: str) -> None:

        if not Result.inited:
            Result.init()

        try:
            self.result = self.find_dept_code(dept_name=dept_name)

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

    def find_dept_code(self, dept_name: str) -> str:

        for key, names in Result.DEPT_CODE.items():
            if dept_name in names:
                return key

        return ''

    def as_json_dict(self) -> dict:
        return {
            'status_code': self.status_code,
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



      


