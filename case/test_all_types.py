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
        self.conninfo = readfiles.read_yaml('dbopration/config.yaml','mysql')
        self.dbconn = mysqlconn.DBOperate(self.conninfo)
        self.sqlpath = 'sqlfiles/mysqlsql/mask_all_types.yaml'
        self.asserts = asserts.Pro_Result(self.sqlpath,self.dbconn)

    def teardown_class(self):
        self.dbconn.conn.close()

    @allure.story('查询全表')
    @allure.testcase('用例ID：1')
    def test_mask_all_type(self):
        assert  False not in self.asserts.assert_result('alltypes')


    @allure.story('charcheck')
    @allure.testcase('用例ID：2')
    def test_charcheck(self):
        assert  False not in self.asserts.assert_result('charcheck')


    @allure.story('charcheck')
    @allure.testcase('用例ID：3')
    def test_charcheck1(self):
        assert  False not in self.asserts.assert_result('charcheck')


    @allure.story('charcheck')
    @allure.testcase('用例ID：3')
    def test_charcheck2(self):
        assert  False not in self.asserts.assert_result('charcheck')



    @allure.story('charcheck')
    @allure.testcase('用例ID：4')
    def test_charcheck3(self):
        assert  False not in self.asserts.assert_result('charcheck')


