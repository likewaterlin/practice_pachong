# -*- coding: utf-8 -*-

import requests


########## cookies操作
# response = requests.get('http://www.baidu.com')
# print(response.cookies)

# #1 将cookies对象转换成字典
# dict_cookies = requests.utils.dict_from_cookiejar(response.cookies)
# print(type(dict_cookies))
# print(dict_cookies)
#
# # 将字典格式的cookies转换成cookiesjar对象
# jar_cookies = requests.utils.cookiejar_from_dict(dict_cookies)
# print(type(jar_cookies))
# print(jar_cookies)

#2 直接cookies操作
# print(response.cookies.get_dict())


##### SSL认证关闭操作
# url = 'https://www.12306.cn/mormhweb/'
# response = requests.get(url, verify=False)
# print(response.content)


##### 设置超时
# url = 'http://www.youtube.com'
# response = requests.get(url, timeout=3)

##### 断言
response = requests.get('http://www.baidu.com')
print(response.status_code)
assert response.status_code == 500


