# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年05月27日 9:52
"""
import os
import json
import time
import win32gui
import win32con
from selenium.webdriver.support.ui import WebDriverWait
from weibo.common.get_log import GetLogger

# 初始化日志对象
log = GetLogger.get_logger(fliename='../log/test_weibo.log')

"""
页面元素操作方法封装
"""
class Base(object):
    # 初始化
    def __init__(self, driver):
        log.info(f'初始化driver：{driver}...')
        self.driver = driver

    # 查找元素方法
    def base_get_element(self, loc, time=30, poll=0.5):
        """
        :param loc: 元素的配置信息，格式为元组
        :param time: 默认超时时间为30秒
        :param poll: 访问频率，默认0.5秒查找一次元素
        :return:返回查找到的元素
        """
        log.info(f'正在查找元素{loc}...')
        try:
            element = WebDriverWait(self.driver, timeout=time,poll_frequency=poll).until(lambda x: x.find_element(*loc))
            return element
        except Exception as e:
            raise e

     # 截图（使用时间戳命名）方法
    def base_get_img(self):
        log.info('正在截图...')
        time.sleep(1)
        self.driver.get_screenshot_as_file(f'../img/{time.strftime("%Y_%m_%d %H_%M_%S")}.png')
        time.sleep(1)

    # 点击方法
    def base_click(self,loc):
        time.sleep(1)
        self.base_get_element(loc).click()
        log.info(f'正在点击元素：{loc}...')

    # 输入方法
    def base_input(self,loc,key):
        time.sleep(1)
        # 定位元素
        ele = self.base_get_element(loc)
        # 进行清空操作
        ele.clear()
        log.info(f'正在给元素：{loc}进行清空...')
        # 进行输入内容
        ele.send_keys(key)
        log.info(f'正在给元素{loc}输入内容：{key}...')

    # 获取元素value值方法
    def base_get_value(self, loc):
        # 使用get_attribute()方法获取指定的元素属性值
        log.info(f'正在获取元素：{loc}文本')
        return self.base_get_element(loc).get_attribute('value')

    # 判断元素是否存在方法
    def base_if_exist(self,loc):
        try:
            self.base_get_element(loc,time=2)
            log.info(f'判断元素：{loc}存在！')
            return True
        except:
            log.info(f'判断元素：{loc}不存在！')
            return False

    # 获取定位内容
    def base_info(self,loc):
        return self.base_get_element(loc)


    # 切换窗口方法
    def base_switch_windows(self):
        handles = self.driver.window_handles
        log.info('正在切换窗口...')
        self.driver.switch_to.window(handles[-1])

    # 关闭窗口
    def base_back(self):
        log.info('正在关闭窗口...')
        self.driver.back()

    # 上传文件方法
    def base_putfile(self,filepath):
        # 打开系统的Windows窗口，从窗口选择本地文件添加
        # 一级顶层窗口
        log.info('正在上传文件...')
        dialog = win32gui.FindWindow("#32770", "打开")
        # 二级窗口
        comboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        # 三级窗口
        comboBox = win32gui.FindWindowEx(comboBoxEx32, 0, "ComboBox", None)
        # 四级窗口 -- 文件路径输入区域
        edit = win32gui.FindWindowEx(comboBox, 0, "Edit", None)
        # 二级窗口 -- 打开按钮
        button = win32gui.FindWindowEx(dialog, 0, "Button", None)
        time.sleep(1)
        # 1、输入文件路径
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)
        time.sleep(1)
        # 2、点击打开按钮
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        log.info('上传成功')

# cookice登录方法
class BaseCookie:
    def __init__(self,path):
        self.path = path

    def base_cookice(self):
        """
        Cookies读取方法
        :param encoding: 文件编码,默认utf-8
        """
        log.info('正在使用cookice登录...')
        if os.path.isfile(self.path):
            with open(self.path, "r", encoding='utf-8') as f:
                cookice = json.load(f)
            return cookice