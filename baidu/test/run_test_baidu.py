# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年05月26日 22:43
"""

# 导包
import pytest
# 运行测试文件并生成测试报告
pytest.main(['-s','test_baidu.py','--alluredir','../report/'])