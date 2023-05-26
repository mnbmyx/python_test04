# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年05月26日 14:38
"""
import time
from lxml import etree

from baidu import base
from baidu.base.base import Base


class Page():
    def __init__(self,driver):
        # 继承Base
        self.driver = Base(driver)
    # 点击方法
    def page_click(self, loc):
        # 调用查找元素，并进行点击
        self.driver.base_get_element(loc).click()

    # 获取value属性方法封装
    def page_get_value(self, loc):
        # 使用get_attribute()方法获取指定的元素属性值
        return self.driver.base_get_element(loc).get_attribute('value')


    # 输入方法
    def page_input(self, loc, key):
        # 调用查找元素，并进行输入
        ele = self.driver.base_get_element(loc)
        ele.clear()
        ele.send_keys(key)

    def page_cookice(self):
        self.driver.base_get_cookice()

    def page_img(self):
        self.driver.base_get_img()




# 页面元素操作层
class PageBaidu():
    def __init__(self,driver):
        self.driver = Page(driver)
    # 弹窗处理
    def page_bd_click(self,loc):
        # 获取当前页面源码
        self.driver.page_click(loc)

    # 文本框输入
    def page_bd_input(self,loc,key):
        self.driver.page_input(loc,key)

    # 点击翻译按钮
    def page_bd_fy(self,loc):
        self.driver.page_click(loc)

    # 添加cookice
    def page_get_cookice(self):
        self.driver.page_cookice()
    # 截图
    def page_get_img(self):
        self.driver.page_img()
