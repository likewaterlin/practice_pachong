# -*- coding: utf-8 -*-

import requests

url = 'https://www.zhihu.com'

headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

}

response = requests.get(url,headers=headers)
print(response.status_code)
print(response.text)