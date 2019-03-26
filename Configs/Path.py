#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 10:55
# @Author  : Zhangyp
# @File    : Path.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import os
import pathlib
import sys


# 取得父路径
def father_path():
	return sys.path[0]


# 由于模块里都会用到log模块，为兼容层级和层外调用，使之都能正确找到路径
def find_path(joinpath):
	"""
	:param joinpath: 被拼接路径,最前面不能以'\'开头，eg:'Log'、'config.log'
	:return: 完成拼接路径
	"""
	path = os.path.join(father_path(), joinpath)
	if pathlib.Path(path).exists():
		return path
	else:
		path = os.path.join(os.path.dirname(father_path()), joinpath)  # 如果当前路径不再就在父路径中找
		return path


# def log_path():
# 	pl = sys.path
# 	for i in range(len(pl)):
# 		path = os.path.join(pl[i], 'Log')
# 		if os.path.exists(path):
# 			return path


def log_path():
	return find_path('Log')

if __name__ == '__main__':
	print(log_path())
	print(find_path('Report'))
