# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年05月27日 9:51
"""
from selenium import webdriver
from time import sleep
from weibo.base.base import BaseCookie
from selenium.webdriver.chrome.service import Service

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


class GetOptions(object):
    # 获取单例driver
    driver = None
    @classmethod
    def get_driver(cls, url,cookice,service):
        if cls.driver is None:
            prefs = {
                'profile.default_content_setting_values': {
                    'notifications': 2  # 隐藏chromedriver的通知
                },
                'credentials_enable_service': False,  # 隐藏chromedriver自带的保存密码功能
                'profile.password_manager_enabled': False  # 隐藏chromedriver自带的保存密码功能
            }
            # 创建一个配置对象
            cls.options = webdriver.ChromeOptions()
            cls.options.add_experimental_option('prefs', prefs)
            cls.options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            cls.driver = webdriver.Chrome(service=Service(service), options=cls.options)
            # 最大化窗口
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(5)
            cls.driver.get(url)
            sleep(4)
            cls.driver.delete_all_cookies()
            # 持久化登录，之后登录就不需要上面的扫二维码
            # login = Base(cookice)
            cookies = BaseCookie(cookice).base_cookice()
            try:
                for cookie in cookies:
                    cookie_dict = {
                        'domain': '.weibo.com',
                        'name': cookie.get('name'),
                        'value': cookie.get('value'),
                        "expires": '',
                        'path': '/',
                        'httpOnly': False,
                        'HostOnly': False,
                        'Secure': False
                    }
                    cls.driver.add_cookie(cookie_dict)
            except Exception as e:
                print(e)
            sleep(2)
            cls.driver.refresh()
            sleep(2)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None