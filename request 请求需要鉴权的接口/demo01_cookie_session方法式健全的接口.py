# -*- encoding: utf-8 -*-
"""
================================
@File    : demo01_cookie_session方法式健全的接口.py
@Time    : 2021/3/24 15:31
@Author  : 测试工程师：刘坤
@Email   : 609127365@qq.com
@Software: PyCharm
================================
"""
"""
http 请求是无状态的
        可以通过，cookie或者token,来传递用户登录的状态信息，
cookie+session进行鉴权的接口，在python的处理：
    requests 模块中有一个session类，使用session类的同一个对象发送请求，会自动保存之前请求的cookie
    信息，

"""
import requests
#创建一个sesion对象
session = requests.Session()
#登录接口
# 接口地址
url = 'https://www.ketangpai.com/UserAPi/login'
# 参数
params = {
    "email": "3247119728@qq.com",
    "password": "nmb12332188",
    "remember": "0"
}
response = session.post(url=url, data=params)
print(response.json())   #没有走通