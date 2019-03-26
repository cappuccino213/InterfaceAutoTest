#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 16:19
# @Author  : Zhangyp
# @File    : ZypLog.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import logging
from logging import handlers
import os


class Logger(object):
	"""
	Log encapsulation
	"""
	level_mappings = {
		'debug': logging.DEBUG,
		'info': logging.INFO,
		'warning': logging.WARNING,
		'error': logging.ERROR,
		'critical': logging.CRITICAL
	}  # Log level relational mapping
	
	def __init__(self, filename, level='info', when='D', back_count=3, fmt='''[时间]:%(asctime)s
[线程]:%(thread)s
[级别]:%(levelname)s
[路径]:%(pathname)s
[函数]:%(funcName)s
[行号]:%(lineno)d
[信息]:%(message)s
------------------
'''):
		"""
		:param filename: log名
		:param level: bug等级
		:param when: 时间间隔单位 S 秒、M 分、H 小时、D 天、W 星期、midnight 每天凌晨
		:param back_count: log保留个数，如果超过这个个数，就会自动删除，
		:param fmt: log格式化
		"""
		self.logger = logging.getLogger(filename)  # set record log as file with name
		self.logger.setLevel(self.level_mappings.get(level))  # set log level
		format_str = logging.Formatter(fmt)  # set the log format
		sh = logging.StreamHandler()  # output to console
		sh.setFormatter(format_str)  # log format of console
		# 按指定时间间隔自动生成文件的处理器
		th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=back_count, encoding='utf-8')
		#  实例化TimedRotatingFileHandler
		th.setFormatter(format_str)  # log format of file
		self.logger.addHandler(sh)  # 把对象加到logger里面
		self.logger.addHandler(th)


if __name__ == '__main__':
	log = Logger(r'%s\Log\all.log' % os.path.dirname(os.getcwd()), level='debug')
	log.logger.debug('this is debug level log')
	log.logger.info('this is info level log')
	log.logger.warning('this is warning level log')
	log.logger.error('this is debug error log')
	log.logger.critical('this is critical level log')
	# error_log = Logger(r'%s\log\error.log' % os.getcwd(), level='error')
	# error_log.logger.error('this is error level log')
