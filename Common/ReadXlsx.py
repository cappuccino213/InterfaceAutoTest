#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 15:19
# @Author  : Zhangyp
# @File    : ReadXlsx.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import xlrd
import json
from Configs.Path import *
from Common.ReadConfig import PARA
from Common import ZypLog


# def get_xlsx(xlsx_name, sheet_name):
# 	"""
#     1.读取xlsx中的case
#     2.将json格式的数据格式化处理（读取出来是str）
#     """
# 	# log = ZypLog.Logger(r'%s\Log\ReadXlsx.log' % PATH, level=PARA['level'])
# 	# log_path = find_path('Log')
# 	log = ZypLog.Logger(r'%s\ReadXlsx.log' % log_path(), level=PARA['level'])
# 	xlsx_path = os.path.join(father_path(), "TestFile", xlsx_name)
# 	file = xlrd.open_workbook(xlsx_path)
# 	sheet = file.sheet_by_name(sheet_name)  # 通过sheet名获取表格
# 	nrows = sheet.nrows
# 	ncols = sheet.ncols
# 	case = []
# 	for i in range(1, nrows):
# 		cls = []
# 		for j in range(ncols):
# 			title = sheet.cell_value(0, j)
# 			value = sheet.cell_value(i, j)
# 			if title in ('headers', 'params', 'data') and value != '':  # headers,params,data这是3个是json格式的
# 				try:
# 					cls.append(json.loads(value))
# 				except Exception as e:
# 					log.logger.error(str(e))
# 			else:
# 				cls.append(value)
# 		log.logger.info('case %s:%s' % (i, cls))
# 		case.append(cls)
# 	return case


def get_xlsx_dict(xlsx_name, sheet_name):
	"""
	1.读取xlsx中的case,转换成dict形式
	2.将json格式的数据格式化处理（读取出来是str）
	"""
	log = ZypLog.Logger(r'%s\ReadXlsx.log' % log_path(), level=PARA['level'])
	case = []
	try:
		# xlsx_path = os.path.join(father_path(), 'TestFile', xlsx_name)
		xlsx_path = os.path.join(find_path('TestFile'), xlsx_name)
		try:
			file = xlrd.open_workbook(xlsx_path)
			sheet = file.sheet_by_name(sheet_name)  # 通过sheet名获取表格
			nrows = sheet.nrows
			ncols = sheet.ncols
			for row in range(1, nrows):
				item = {}
				for col in range(ncols):
					title = sheet.cell_value(0, col)
					value = sheet.cell_value(row, col)
					if title in ('headers', 'params', 'data') and value != '':
						item[title] = json.loads(value)
					else:
						item[title] = value
				case.append(item)
				log.logger.info('case %s:%s' % (row, item))
		except Exception as e:
			log.logger.error(str(e))
	except Exception as e:
		log.logger.error(str(e))
	finally:
		return case


if __name__ == '__main__':
	xls1 = get_xlsx_dict('testcase.xlsx', 'POD_API')
	print(xls1)

