# -*- coding: utf-8 -*-


from selenium import webdriver

url = 'http://www.baidu.com'

dr = webdriver.Chrome()

dr.implicitly_wait(10)

dr.get(url)

el = dr.find_element_by_xpath('//*[@id="lg"]/map/areas')

# 尝试读写这段代码发现不是很明白最后一句是什么意思，是悬停在某个地方么？






