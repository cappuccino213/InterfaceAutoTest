#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 16:21
# @Author  : Zhangyp
# @File    : ConfigMysql.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import pymysql.cursors
# from Configs.config import PARA
from Common.ReadConfig import PARA
from Configs.Path import *
from Common.ZypLog import Logger

class MYSQL:
	def __init__(self):
		self.host = PARA['host']
		self.user = PARA['user']
		self.pwd = PARA['password']
		self.db = PARA['dbname']
		self.log = Logger(r'%s\db.log' % log_path(), level=PARA['level'])
	
	def __GetConnect(self):
		# if not self.db:
		# 	raise (NameError, "Error setting database parameter")
		# self.conn = pymysql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="utf8")
		# cur = self.conn.cursor()
		# if not cur:
		# 	raise (NameError, "Failed to connect to database")
		# else:
		# 	return cur
		try:
			self.conn = pymysql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db,
										charset="utf8")
			self.log.logger.info('Connect DB successfully!')
		except Exception as e:
			self.log.logger.error(str(e))
		else:
			cur = self.conn.cursor()
			return cur
	
	def ExecQuery(self, sql):
		cur = self.__GetConnect()
		try:
			cur.execute(sql)
			self.log.logger.info('Query Successfully!')
			resList = cur.fetchall()
			return resList
		except AttributeError as e:
			self.log.logger.Error(str(e))
		finally:
			self.conn.close()
	
	def ExceUpdate(self, sql):
		cur = self.__GetConnect()
		try:
			cur.execute(sql)
			self.conn.commit()
		except Exception:
			self.conn.rollback()
		finally:
			self.conn.close()


if __name__ == '__main__':
	zypsql = MYSQL()
	sql = "select * from exampublish where ExamineID='48'"
	l = zypsql.ExecQuery(sql)
	print(l)
