#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 15:15
# @Author  : Zhangyp
# @File    : conftest.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import pytest
from datetime import datetime
from py._xmlgen import html

"""
自定义报告格式
详细用法可见https://pypi.org/project/pytest-html/
"""


# 编辑报告中的Environment
def pytest_configure(config):
	config._metadata['Test IP'] = '192.168.1.27'


# 编辑Summary
@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
	prefix.extend([html.p("QA: zhangyp")])  # 第一行
	# summary.extend([html.p("foo: bar")])  #
	# postfix.extend([html.p("foo: bar")])  #最后一行


# 编辑报告表头
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
	cells.insert(2, html.th('Description'))
	cells.insert(4, html.th('Time', class_='sortable time', col='time'))
	cells.pop()

# 编辑报告数据
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
# 	cells.insert(2, html.td(report.description))
# 	cells.insert(4, html.td(datetime.utcnow(), class_='col-time'))
# 	cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
	outcome = yield
	report = outcome.get_result()
	report.description = str(item.function.__doc__)

