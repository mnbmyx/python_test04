# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年05月26日 14:11
"""
import time

from selenium.webdriver.support.ui import WebDriverWait
from baidu.log.get_log import GetLogger
'''
这里我们定义一个Base类，对Selenium WebDriver提供的API进行二次封装；
'''
log = GetLogger.get_logger(fliename='../log/test_baidu.log')

class Base(object):
    def __init__(self, driver):
        log.info(f'初始化driver{driver}')
        self.driver = driver

    def base_get_element(self, loc, time=30, poll=0.5):
        """
        :param loc: 元素的配置信息，格式为元组
        :param time: 默认超时时间为30秒
        :param poll: 访问频率，默认0.5秒查找一次元素
        :return:返回查找到的元素
        """
        log.info(f'正在查找元素{loc}')
        try:
            element = WebDriverWait(self.driver, timeout=time,poll_frequency=poll).until(lambda x: x.find_element(*loc))
            return element
        except Exception as e:
            raise e

    def base_get_elements(self, loc, time=30, poll=0.5):
        """
        :param loc: 元素的配置信息，格式为元组
        :param time: 默认超时时间为30秒
        :param poll: 访问频率，默认0.5秒查找一次元素
        :return:返回查找到的元素
        """
        try:
            elements = WebDriverWait(self.driver, timeout=time, poll_frequency=poll).until(
                lambda x: x.find_elements(*loc))
            return elements
        except Exception as e:
            raise e
    # 获取cookice
    def base_get_cookice(self):
        log.info('正在使用cookice进行登录')
        # 添加cookice
        self.driver.add_cookie({'name': 'BDUSS',
                                'value': 'EY1N1pXNHpXN35PYjI1Mk1uSkNRTk42Z0dmUVNZQk9wNkhrWEZueU56bjMxV2xrSVFBQUFBJCQAAAAAAAAAAAEAAABWBnCHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPdIQmT3SEJkN'})
        # 刷新页面登录成功
        self.driver.refresh()

     # 截图
    def base_get_img(self):
        log.info('正在截图')
        self.driver.get_screenshot_as_file(f'../img/{time.strftime("%Y_%m_%d %H_%M_%S")}.png')