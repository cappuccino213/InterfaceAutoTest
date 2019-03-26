#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 10:32
# @Author  : Zhangyp
# @File    : ConfigHttp.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
# from Common.ReadConfig import conf, PATH  # gets the parent path & time function
from Common.ReadConfig import PARA
from Common import ZypLog
import requests
from Configs.Path import *
# import os
from Common.ConfigToken import get_token


class ConfigHttp:
	"""
	HTTP configuration
	"""
	
	def __init__(self):
		global host, port, timeout
		host = PARA['baseurl']
		port = PARA['port']
		timeout = PARA['timeout']
		# self.log = ZypLog.Logger(r'%s\Log\ConfigHttp%s.log' % (PATH, dt), level='debug') #日志重新生成
		# self.log = ZypLog.Logger(r'%s\Log\ConfigHttp.log' % (os.path.dirname(os.getcwd())), level=PARA['level'])
		self.log = ZypLog.Logger(r'%s\ConfigHttp.log' % log_path(), level=PARA['level'])
		self.headers = {}  # Define key-value pairs (dictionaries)
		self.params = {}
		self.data = {}
		self.url = None
	
	# self.files = {}
	
	#  Assign values to parameters
	def set_url(self, url):
		self.url = host + port + url
		self.log.logger.info("type:%s value:%s" % (type(self.url), self.url))
	
	def set_headers(self, header):
		self.headers = header
		self.log.logger.info("type:%s value:%s" % (type(self.headers), self.headers))
	
	def set_params(self, param):
		self.params = param
		self.log.logger.info("type:%s value:%s" % (type(self.params), self.params))
	
	def set_data(self, data):
		self.data = data
		self.log.logger.info("type:%s value:%s" % (type(self.data), self.data))
	
	# def set_files(self, file):
	# 	self.files = file
	
	#  defined http get method
	def get(self):
		try:
			response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(timeout))
			return response
		except TimeoutError as e:
			self.log.logger.info(str(e))
			return None
	
	# defined http post method
	def post(self):
		try:
			response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(timeout))
			return response
		except TimeoutError as e:
			self.log.logger.info(str(e))
			return None


if __name__ == '__main__':
	H = {'Accept': 'application/json, text/plain, */*', 'Authorization': get_token()}
	cfh1 = ConfigHttp()
	cfh1.set_url('/Exam/GetExamList')
	cfh1.set_headers(H)
	cfh1.set_data({"examInfo": {"medRecNo": "", "patientID": "", "accessionNumber": "", "examType": [],
								"patientName": "", "hasFilm": "", "isPrinted": "", "dicomPeerIDList": [],
								"examStartDate": "2019-02-01 00:00:00", "examEndDate": "2019-02-01 23:59:59"},
				   "pageInfo": {"pageIndex": 1, "pageSize": 10},
				   "orderInfo": {"columnName": "RequestTime", "orderType": 0}})
	r1 = cfh1.post()
	print(r1.status_code, r1.content)
