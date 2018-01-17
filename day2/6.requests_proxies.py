# -*- coding: utf-8 -*-

import requests

# 构建url

url = 'http://diy.pconline.com.cn'

# 构建请求头

headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'

}

# 构建免费代理
proxies = {
    'http':'http://118.254.150.176:3128',
    'https':'https://118.254.150.176:3128',
}

# 收费代理

# proxies = {
#     'http':'http://morganna_mode_g:ggc22qxp@117.48.214.246:16186',
#     'https':'https://morganna_mode_g:ggc22qxp@117.48.214.246:16186',
#
# }

# 发送请求获取响应
response = requests.get(url,headers=headers,proxies=proxies)

# 如何验证代理是否使用成功

