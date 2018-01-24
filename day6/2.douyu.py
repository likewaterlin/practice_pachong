# -*- coding: utf-8 -*-
import json
import time
from selenium import webdriver


class Douyu(object):

    def __init__(self):

        self.url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()

        self.file = open('douyuonline.json', 'w')

    def prase_data(self):
        node_list = self.driver.find_elements_by_xpath('//*[@id="live-list-contentbox"]/li/a')
        data_list = list()

        for node in node_list:
            temp = dict()
            temp['title'] = node.find_element_by_xpath('./div/div/h3').text
            temp['category'] = node.find_element_by_xpath('./div/div/span').text
            temp['owner'] = node.find_element_by_xpath('./div/p/span[1]').text
            temp['num'] = node.find_element_by_xpath('./div/p/span[2]').text
            temp['cover'] = node.find_element_by_xpath('./span/img').get_attribute('data-original')
            temp['link'] = node.get_attribute('href')
            data_list.append(temp)
        print(data_list)
        return data_list

    def save_data(self, data_list):
        for data in data_list:
            str_data = json.dumps(data, ensure_ascii=False) + ',\n'
            self.file.write(str_data)

    def __del__(self):
        self.driver.close()
        self.file.close()

    def run(self):

        # 创建url
        # 创建浏览器对象
        self.driver.get(self.url)
        while True:
            # 发送请求，接收数据解析
            data_list = self.prase_data()
            # 保存数据
            self.save_data(data_list)
            try:
                el_next = self.driver.find_element_by_xpath('//a[@class="shark-pager-next"]')
                el_next.click()
                time.sleep(3)
            except:
                break


if __name__ == '__main__':
    douyu = Douyu()
    douyu.run()
