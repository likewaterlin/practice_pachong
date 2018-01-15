# -*- coding: utf-8 -*-

# 构建url
import requests

url = 'http://www.xiami.com/search'

# 构建请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'
}

# 构建参数
# target_url = url+ 'key=陈奕迅'

# 参数的形式
data = {
    'key':'周深'
}

#发送请求获取响应
response = requests.get(url,headers=headers,params=data)

# 保存源码
with open('xiami1.html','wb') as f:
    f.write(response.content)
