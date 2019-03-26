#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 11:29
# @Author  : Zhangyp
# @File    : ConfigToken.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import requests

HEADERS = {'Content-Type': 'application/json'}


def new_key():
	url = 'http://192.168.1.19:6001/openkey/new'
	body = "{'key':'6B5906ED-36B4-4572-ABE5-7DACE5B03080'," \
		   "'ClientIP':'192.168.1.18'," \
		   "'OnlineCount':50," \
		   "'SessionExpire':120," \
		   "'UserRequestExpireSession':false}"
	r = requests.post(url, headers=HEADERS, data=body)
	return r.text


def get_token():
	url = 'http://192.168.1.19:6001/token/retrive'
	audience = new_key()
	# audience = "5D47E01B49294D86970AE662D144BAD3"
	body = "{'UniqueIdentity':'zyp','Audience':%s,'CustomData':'','Expire':2}" % audience
	r = requests.post(url, headers=HEADERS, data=body)
	return r.json()['token']


if __name__ == '__main__':
	print(get_token())
	