from pywebio.input import input, FLOAT, TEXT
from pywebio.output import put_text, put_table
import requests

def main_one():
    prefix = input("Input prefix：", type=TEXT)
    url = f'http://0.0.0.0:18000/get_suggestions/{prefix}'
    resp = requests.get(url)
    assert  200 <= resp.status_code < 300
    res_list = resp.json()['result']
    put_text(str(res_list))
    res_tablex = [[it] for it in res_list]
    put_table(res_tablex)

def main_loop():
    

if __name__ == '__main__':
    main_loop()
    input("press enter to finish")