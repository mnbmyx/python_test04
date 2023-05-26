# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年05月26日 14:38
"""
from selenium import webdriver


class GetDriver(object):
# 获取单例driver
    driver = None
    @classmethod
    def get_driver(cls,url):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(url)
        return cls.driver



    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None