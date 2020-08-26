# -*- coding:utf-8 -*-
'''
@Time       : 2020/8/5 19:50
@Author     : Joy
@FileName   : test_all_types.py
'''


import allure
from dbopration import mysqlconn
from common import readfiles,asserts


@allure.feature('测试全字段表')
class TestAllTypes:

    def setup_class(self):
        # 获取数据库连接对象
        self.conninfo = readfiles.read_yaml('dbopration\config.yaml','mysql')
        self.dbconn = mysqlconn.DBOperate(self.conninfo)
        self.sqlpath = 'sqlfiles\mysqlsql\mask_all_types.yaml'
        self.asserts = asserts.Pro_Result(self.sqlpath,self.dbconn)

    def teardown_class(self):
        self.dbconn.conn.close()


    @allure.story('全字段')
    def test_mask_all_type(self):
        assert  False not in self.asserts.assert_result('alltypes')


    @allure.story('charcheck')
    def test_charcheck(self):
        assert  False not in self.asserts.assert_result('charcheck')


    @allure.story('varcharcheck')
    def test_varcharcheck(self):
        assert  False not in self.asserts.assert_result('varcharcheck')

    @allure.story('binarycheck')
    def test_binarycheck(self):
        assert  False not in self.asserts.assert_result('binarycheck')


    @allure.story('varbinarycheck')
    def test_varbinarycheck(self):
        assert  False not in self.asserts.assert_result('varbinarycheck')

    @allure.story('tinyblobcheck')
    def test_tinyblobcheck(self):
        assert  False not in self.asserts.assert_result('tinyblobcheck')


    @allure.story('blobcheck')
    def test_blobcheck(self):
        assert  False not in self.asserts.assert_result('blobcheck')


    @allure.story('mediumblobcheck')
    def test_mediumblobcheck(self):
        assert  False not in self.asserts.assert_result('mediumblobcheck')

    @allure.story('longblobcheck')
    def test_longblobcheck(self):
        assert  False not in self.asserts.assert_result('longblobcheck')

    @allure.story('tinytextcheck')
    def test_tinytextcheck(self):
        assert  False not in self.asserts.assert_result('tinytextcheck')

    @allure.story('textcheck')
    def test_textcheck(self):
        assert  False not in self.asserts.assert_result('textcheck')

    @allure.story('mediumtextcheck')
    def test_mediumtextcheck(self):
        assert  False not in self.asserts.assert_result('mediumtextcheck')

    @allure.story('longtextcheck')
    def test_longtextcheck(self):
        assert  False not in self.asserts.assert_result('longtextcheck')

    @allure.story('enumcheck')
    def test_enumcheck(self):
        assert  False not in self.asserts.assert_result('enumcheck')

    @allure.story('bitcheck')
    def test_bitcheck(self):
        assert  False not in self.asserts.assert_result('bitcheck')

    @allure.story('tinyintcheck')
    def test_tinyintcheck(self):
        assert  False not in self.asserts.assert_result('tinyintcheck')

    @allure.story('smallintcheck')
    def test_smallintcheck(self):
        assert  False not in self.asserts.assert_result('smallintcheck')

    @allure.story('mediumintcheck')
    def test_mediumintcheck(self):
        assert  False not in self.asserts.assert_result('mediumintcheck')

    @allure.story('intcheck')
    def test_intcheck(self):
        assert  False not in self.asserts.assert_result('intcheck')

    @allure.story('integercheck')
    def test_integercheck(self):
        assert  False not in self.asserts.assert_result('integercheck')

    @allure.story('bigintcheck')
    def test_bigintcheck(self):
        assert  False not in self.asserts.assert_result('bigintcheck')

    @allure.story('serialcheck')
    def test_serialcheck(self):
        assert  False not in self.asserts.assert_result('serialcheck')

    @allure.story('timecheck')
    def test_timecheck(self):
        assert  False not in self.asserts.assert_result('timecheck')

    @allure.story('datetimecheck')
    def test_datetimecheck(self):
        assert  False not in self.asserts.assert_result('datetimecheck')

    @allure.story('yearcheck')
    def test_yearcheck(self):
        assert  False not in self.asserts.assert_result('yearcheck')

    @allure.story('timestampcheck')
    def test_timestampcheck(self):
        assert  False not in self.asserts.assert_result('timestampcheck')

    @allure.story('numericcheck')
    def test_numericcheck(self):
        assert  False not in self.asserts.assert_result('numericcheck')

    @allure.story('decimalcheck')
    def test_decimalcheck(self):
        assert  False not in self.asserts.assert_result('decimalcheck')