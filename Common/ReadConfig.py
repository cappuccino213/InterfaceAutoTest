#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 14:16
# @Author  : Zhangyp
# @File    : ReadConfig.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import configparser
from Configs.Path import *
from Common import ZypLog

"""
read config.ini as dict (each parameter name cannot be the same)
eg:s = conf()
   s['http']
"""


def conf():
	
	"""
	处理BOM字符（当配置文件被记事本编辑过后，会插入一个bom头）
	"""
	# logpath = find_path('Log')
	# log = ZypLog.Logger(r'%s\config.log' % logpath, level='info')
	log = ZypLog.Logger(r'%s\config.log' % log_path(), level='info')
	try:
		bom = b'\xef\xbb\xbf'
		# with open(r'%s\Configs\config.ini' % father_path(), 'r+b') as f:
		with open(r'%s\config.ini' % find_path('Configs'), 'r+b') as f:
			if bom == f.read(3):
				content = f.read()
				f.seek(0)
				f.write(content)
				f.truncate()
	except (FileNotFoundError, FileExistsError) as e:
		log.logger.error(str(e))
	try:
		cf = configparser.ConfigParser()
		# cf.read(r'%s\Configs\config.ini' % father_path(), encoding='utf-8')
		cf.read(r'%s\config.ini' % find_path('Configs'), encoding='utf-8')
		section = cf.sections()
		kv = []
		for i in range(len(section)):
			kv = kv + cf.items(section[i])
		s = dict((x, y) for x, y in kv)  # 将tuple转化成dict
		log.logger.info('read config:%s' % s)
		return s
	except Exception as e:
		log.logger.error(str(e))


PARA = conf()

if __name__ == '__main__':
	print(conf())
