#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 14:38
# @Author  : Zhangyp
# @File    : test_httpAPI.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import pytest
import json
from Common.ConfigHttp import ConfigHttp
from Common.ConfigToken import get_token
# from Common.ReadXlsx import get_xlsx
from Common.ReadXlsx import get_xlsx_dict
from Configs.config import *


def sort_by_method(xlsx_name, sheet_name):
    """
    将获取到的case根据http方法，分别归类后放入各自的list：数据结构为{'get':[{'case_name':''},{}...],'post':[{'case_name':''},{}..]}
    """
    case = get_xlsx_dict(xlsx_name, sheet_name)
    get_list = []
    post_list = []
    sort_case = {}
    for i in range(len(case)):
        if case[i]['method'] == 'get':
            get_list.append(case[i])
        if case[i]['method'] == 'post':
            post_list.append(case[i])
    sort_case['get'] = get_list
    sort_case['post'] = post_list
    return sort_case


# 为方便之后的赋值取个case字典的别名
C = sort_by_method(PARA['xlsxname'], PARA['sheetname'])


# 用于判定case是否测试通过
def judge(http_code, http_msg, code, msg):
    """
    :param http_code: http返回的代码
    :param http_msg: http返回的描述信息
    :param code: case中设定的代码
    :param msg: case中设定的信息
    :return: 两者都符合返回True
    """
    if http_code == code:
        if http_msg == msg:
            return True
        else:
            return False
    else:
        return False


# 通过params函数实现fixture的参数化
@pytest.fixture(params=C['get'])
def get_case(request):
    return request.param


@pytest.fixture(params=C['post'])
def post_case(request):
    return request.param


# 以下时具体的测试script
def test_get(get_case):
    cfh = ConfigHttp()
    cfh.set_url(get_case['url'])
    if get_case['token'] == 1:  # 判断接口是否需要传入token
        get_case['headers']['authorization'] = get_token()  # 当token=1时，将token的值传入headers
    cfh.set_headers(get_case['headers'])
    cfh.set_params(get_case['params'])
    r = cfh.get()
    text = json.loads(r.text)
    assert judge(r.status_code, text['status'], get_case['code'], get_case['msg'])


def test_post(post_case):
    cfh = ConfigHttp()
    cfh.set_url(post_case['url'])
    if post_case['token'] == 1:  # 判断接口是否需要传入token
        post_case['headers']['authorization'] = get_token()  # 当token=1时，将token的值传入headers
    cfh.set_data(post_case['data'])
    r = cfh.post()
    text = json.loads(r.text)
    assert judge(r.status_code, text['status'], post_case['code'], post_case['msg'])


if __name__ == '__main__':
    pytest.main()
# sort_by_method('testcase.xlsx', 'POD_API')
