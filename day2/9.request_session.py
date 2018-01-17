# -*- coding: utf-8 -*-

import requests
import re

# 构建url
url = 'http://www.renren.com/PLogin.do'
# 构建请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0',

}


# 构建表单数据
post_data = {
    "email": "17173805860",
    "password": "1qaz@WSX3edc",
}

# 实例化session对象
session =requests.session()
# 发送请求获取响应
session.post(url,headers=headers, data=post_data)

# 验证登陆
response = session.get('http://www.renren.com/923768535')
print((re.findall('迷途',response.content.decode())))