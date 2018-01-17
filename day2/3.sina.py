# -*- coding: utf-8 -*-


import requests

url = 'http://www.sina.com.cn'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'
}

response = requests.get(url, headers=headers)

print(response.content.decode())