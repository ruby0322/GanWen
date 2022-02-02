import json
import requests


def fetch_data(fetch_url: str) -> dict:
    return json.loads(
        requests.get(
            fetch_url
        ).text
    )

def main() -> int:

    print('你好呀！，這是一個呼叫台大系所查詢API的範例程式碼。')

    while (query_type := input('請輸入搜尋種類（dept_name_api / dept_code_api）：')) not in ['dept_name_api', 'dept_code_api']:
        print('無效的輸入')

    if query_type == 'dept_name_api':
        dept_code = input('請輸入系所代碼：')
        name_format = input('請輸入系所名稱格式（short / full）（選填）：')
        params_str = f'{dept_code=}&{name_format=}'.replace('\'', '')
    else:
        dept_name = input('請輸入系所名稱：')
        params_str = f'{dept_name=}'.replace('\'', '')
    
    fetch_url = f'https://ntu-dept-code.herokuapp.com/{query_type}?{params_str}'
    print(f'{fetch_url=}')
    print(fetch_data(fetch_url))
    return 0

if __name__ == '__main__':
    main()
    