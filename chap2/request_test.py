"""使用requests库"""

import requests
import re
from requests.auth import HTTPBasicAuth

"GET方法"
# data = {
#     'name': 'germey',
#     'age': 25
# }

# r = requests.get('http://httpbin.org/get', params=data)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))

"用正则表达式选取页面部分"
# r = requests.get('https://static1.scrape.center/')
# pattern = re.compile('<h2.*?>(.*?)</h2>')
# titles = re.findall(pattern, r.text)
# print(titles)

"用GET获取二进制数据"
# r = requests.get('https://www.runoob.com/favicon.ico')
# print(r.text)
# print(r.content)
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

"用GET增加请求头"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get('https://static1.scrape.center/', headers=headers)
# print(r.text)

"POST方法"
# data = {'name': 'germey', 'age': '25'}
# r = requests.post("http://httpbin.org/post", data=data)
# print(r.text)
# print(type(r.text))

"获取状态码"
# r = requests.get('https://static1.scrape.center/')
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)
# exit() if not r.status_code == requests.codes.ok else print('Request Successfully')

"在POST方法中提交文件"
# files = {'file': open('./favicon.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)

"获取和使用Cookies"
# r = requests.get('http://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)

# headers = {
#     'Cookie': '_octo=GH1.1.1245948438.1636553190; tz=Asia/Shanghai; _device_id=95982a0e374bf4a01e12273567a53bb1; has_recent_activity=1; user_session=zPE9PiSYfw_NUdbYha2AqfKxFEmW-nis5G-D2Zv07k8WSCw9; __Host-user_session_same_site=zPE9PiSYfw_NUdbYha2AqfKxFEmW-nis5G-D2Zv07k8WSCw9; tz=Asia/Shanghai; color_mode={"color_mode":"light","light_theme":{"name":"light","color_mode":"light"},"dark_theme":{"name":"dark","color_mode":"dark"}}; logged_in=yes; dotcom_user=MidoQ; _gh_sess=4Mm4laYMU26EoJnOyrjn6rc6M6wxvxbBn9VgCjqf3P5CXlNiQtla+FWpmCSvkjzXe6tviNRYBHZC/jBw9BDfB80Oofbh3ZKDGiJFKptAFtx5tt8zsTIxnl5QSVWBufxtHt0LYy/5r4iAQ9+WB3Q/9TLhNYt6o7WkYBgCybRzVRK9m8zCWo0F3GfCrxRUIZuPerPXcPqnc3ARwCM/urG4wxyFWYK1csKJ3ovq+PxtspZHOCk+9a3YjY9n7qFml+aQR08LuxiW2cIsfbZNm3ZGTPtkBF+zxm1/I5MzqGvFJM8LIN+qn8Z5uqSFTFZ0uDbz6uQttJuCRSddfbyVaniPi6RYiikBSaz9DWm5C/fvdgLQkWJ0ciKbbQRZR9sECkICF6cn92MDIkdTlluBDmi42kyDaXtURHwzZ01PZs5MUxf3EoZV5hx++GDHfWJlYA5YJhmsnlKeZPeU666q2Art5mvmiMNPC3iXchB0lg2iJm8L/GcnBg3Y5p0Hpao1nY6wt4T2OsMPG/1vWXL550NtfTAhZ7fXODhhI8cmNuhLSS3APG37zMalLrz5tWWgga695dYvcnhztsXOiG7XfQZwarq18cXhxrIDU7qsNnlMcJbcng59tHJKzXPaVzdUGLPrv9acHbG28LjtjbxSYqdOIFjbVvZybhAvvq3SRKdeLR+F4+g++z7wUGL3Un1GK7sd83Icu81prlelPxaacidLB1YH6aIcgYnAO5X4XtKBaNfZW67Uknqq1kYon71IA2GeuyEUpg3L65kkPtcVPCRlKijafKELIeu5exD9VZ3/ypXykN6pcXvvzK2BXG9xxPgqcFwgttd4BFxx2CVqjY/7LpAYdv2yBGnQrNe59Y7FgR+NJH/Ri+RU4AvVxzuXOk2mOOHqwBnXfzs/82wPXQrucXzF220=--4AsUCTmAQ56GK4Ep--E0jgAv6DqluWkOY/lPz4lg==',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
# }
# r = requests.get('https://github.com/', headers=headers)
# print(r.text)

"维持Session"
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

"超时设置"
# r = requests.get('https://httpbin.org/get', timeout=1)  # 连接和读取时间总和
# r = requests.get('https://httpbin.org/get', timeout=(5, 30))    # 连接和读取分别设置

"基本身份认证 HTTP Basic Access Authentication"
r = requests.get('https://static3.scrape.center/', auth=HTTPBasicAuth('admin', 'admin'))
print(r.status_code)
