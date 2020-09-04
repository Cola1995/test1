"""
标加函数的三种方法
1.显示执行函数名，::
命令行执行
eg： pytest test_02.py::test01
2.使用模糊匹配 -K标识
eg:pytest -k add test_02.py
3.使用markers 函数，给函数增加装饰器
新建.ini文件
eg: pytest -m do test_02.py
"""

import pytest
def test01():
    print("test01111")


def test02():
    print("test022222")

@pytest.mark.do
def test_add():
    print("add")

@pytest.mark.do
def test_sub():
    print("test_sub11111")