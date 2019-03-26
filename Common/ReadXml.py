#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 15:56
# @Author  : Zhangyp
# @File    : ReadXml.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from Configs.Path import *

try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

database = {}
"""
从xml文件中获取sql语句
"""

def set_xml():
	"""
    Read the SQL statement from the XML file
    """
	if not database:  # if dict isEmpty
		sql_path = os.path.join(find_path("TestFile"), 'sql.xml')
		tree = ET.parse(sql_path)
		for db in tree.findall("database"):
			db_name = db.get("name")
			table = {}
			for tb in db.getchildren():
				table_name = tb.get("name")
				sql = {}
				for data in tb.getchildren():
					sql_id = data.get("id")
					sql[sql_id] = data.text
				table[table_name] = sql
			database[db_name] = table


def get_xml_dict(database_name, table_name):
	"""
	get sql statement as dict
	"""
	set_xml()
	database_dict = database.get(database_name).get(table_name)
	return database_dict


def get_sql(database_name, table_name, sql_id):
	"""
	get the specified SQL statement
	"""
	db = get_xml_dict(database_name, table_name)
	sql = db.get(sql_id)
	return sql


if __name__ == '__main__':
	print(get_sql('eWordPOD', 'VP_FilmSample', 'delete_filmsample'))
