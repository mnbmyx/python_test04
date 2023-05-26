# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年05月27日 9:52
"""


from weibo.base.base import Base

"""
页面元素操作层
"""

class PageLogin(Base):
    # 点击方法
    def page_click(self, loc):
        self.base_click(loc)

    # 输入方法
    def page_input(self, loc, key):
        self.base_input(loc,key)

    # 截图
    def page_get_img(self):
        self.base_get_img()

    # 切换窗口
    def page_switch_windows(self):
        self.base_switch_windows()

    # 获取定位内容
    def page_info(self,loc):
        return self.base_info(loc)

    # 上传文件
    def page_putfile(self,filepath):
        self.base_putfile(filepath)