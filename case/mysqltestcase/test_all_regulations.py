# -*- coding:utf-8 -*-
'''
@Time       : 2020/8/5 19:50
@Author     : Joy
@FileName   : test_all_types.py
'''


import allure
from dbopration import mysqlconn
from common import readfiles,asserts


@allure.feature('全字段表')
class TestAllTypes:

    def setup_class(self):
        # 获取数据库连接对象
        self.conninfo = readfiles.read_yaml('dbopration\config.yaml','mysql')
        self.dbconn = mysqlconn.DBOperate(self.conninfo)
        self.sqlpath = 'sqlfiles\mysqlsql\mask_all_types.yaml'
        self.asserts = asserts.Pro_Result(self.sqlpath,self.dbconn)

    def teardown_class(self):
        self.dbconn.conn.close()





