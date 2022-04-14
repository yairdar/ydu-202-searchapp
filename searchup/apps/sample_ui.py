from pywebio.input import input, FLOAT, TEXT
from pywebio.output import put_text, put_table
import requests

def main_loop():
    prefix = input("Input prefix：", type=TEXT)
    url = f'http://0.0.0.0:18000/get_suggestions/{prefix}'
    resp = requests.get(url)
    assert  200 <= resp.status_code < 300
    res_list = resp.json()['result']
    put_text(str(res_list))
    res_tablex = [[it] for it in res_list]
    put_table(res_tablex)
    # weight = input("Input your weight(kg)：", type=FLOAT)

    # BMI = weight / (height / 100) ** 2

    # top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
    #               (25, 'Normal'), (30, 'Overweight'),
    #               (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

    # for top, status in top_status:
    #     if BMI <= top:
    #         put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
    #         put_table([["name"], ["A"], ["B"]])
    #         break

if __name__ == '__main__':
    main_loop()
    input("press enter to finish")