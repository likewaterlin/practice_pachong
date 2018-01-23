# -*- coding: utf-8 -*-


#coding:utf-8
from selenium import webdriver

url = 'http://sh.58.com/'
# 构建浏览器对象
dr = webdriver.Chrome()

# 加载url对相应的响应
dr.get(url)

print(dr.current_url)
print(dr.window_handles)
# 模拟点击房屋出租(指向到需要选择的元素，并使用el.click()进行点击操作)
el = dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/em[1]/a')
el.click()

# 切换到某窗口此句有不明之处
dr.switch_to.window(dr.window_handles[-1])
print(dr.current_url)
print(dr.window_handles)

# 定位所有title
node_list = dr.find_elements_by_xpath('/html/body/div[3]/div[1]/div[5]/div[2]/ul/li/div[2]/h2/a')
for node in node_list:
    # 将所有的描述和链接打印出来
    print(node.text, node.get_attribute('href'))