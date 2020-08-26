# -*-coding:utf-8-*-
'''
@Time       : 2020/8/5 19:50
@Author     : Joy
@FileName   : test_all_types.py
'''



import allure
from dbopration import mysqlconn
from common import readfiles,asserts

@allure.feature("mysql函数测试")
class TestAllFunctions:

    def setup_class(self):
        # 获取数据库连接对象
        self.conninfo = readfiles.read_yaml('dbopration\config.yaml','mysql')
        self.dbconn = mysqlconn.DBOperate(self.conninfo)
        self.sqlpath = 'sqlfiles\mysqlsql\other_select.yaml'
        self.asserts = asserts.Pro_Result(self.sqlpath,self.dbconn)

    def teardown_class(self):
        self.dbconn.conn.close()

    @allure.story('测试ABS')
    def test_abs_function(self):
        assert  False not in self.asserts.assert_general('ABS')

    @allure.story('测试MOD')
    def test_ABS_function(self):
        assert  False not in self.asserts.assert_general('MOD')

    @allure.story('测试CEILING')
    def test_CEILING_function(self):
        assert  False not in self.asserts.assert_general('CEILING')

    @allure.story('测试ROUND')
    def test_ROUND_function(self):
        assert  False not in self.asserts.assert_general('ROUND')

    @allure.story('测试POW')
    def test_POW_function(self):
        assert  False not in self.asserts.assert_general('POW')

    @allure.story('测试POWER')
    def test_POWER_function(self):
        assert  False not in self.asserts.assert_general('POWER')

    @allure.story('测试FLOOR')
    def test_FLOOR_function(self):
        assert  False not in self.asserts.assert_general('FLOOR')

    @allure.story('测试RAND')
    def test_RAND_function(self):
        assert  False not in self.asserts.assert_general('RAND')

    @allure.story('测试ASCII')
    def test_ASCII_function(self):
        assert  False not in self.asserts.assert_general('ASCII')

    @allure.story('测试CONCAT')
    def test_CONCAT_function(self):
        assert  False not in self.asserts.assert_general('CONCAT')

    @allure.story('测试LENGTH')
    def test_LENGTH_function(self):
        assert  False not in self.asserts.assert_general('LENGTH')

    @allure.story('测试LOCATE')
    def test_LOCATE_function(self):
        assert  False not in self.asserts.assert_general('LOCATE')

    @allure.story('测试INSTR')
    def test_INSTR_function(self):
        assert  False not in self.asserts.assert_general('INSTR')

    @allure.story('测试LEFT')
    def test_LEFT_function(self):
        assert  False not in self.asserts.assert_general('LEFT')

    @allure.story('测试RIGHT')
    def test_RIGHT_function(self):
        assert  False not in self.asserts.assert_general('RIGHT')

    @allure.story('测试SUBSTRING')
    def test_SUBSTRING_function(self):
        assert  False not in self.asserts.assert_general('SUBSTRING')

    @allure.story('测试REPEAT')
    def test_REPEAT_function(self):
        assert  False not in self.asserts.assert_general('REPEAT')

    @allure.story('测试REVERSE')
    def test_REVERSE_function(self):
        assert  False not in self.asserts.assert_general('REVERSE')

    @allure.story('测试INSERT')
    def test_INSERT_function(self):
        assert  False not in self.asserts.assert_general('INSERT')

    @allure.story('测试LOWER')
    def test_LOWER_function(self):
        assert  False not in self.asserts.assert_general('LOWER')

    @allure.story('测试UPPER')
    def test_UPPER_function(self):
        assert  False not in self.asserts.assert_general('UPPER')

    @allure.story('测试BIN')
    def test_BIN_function(self):
        assert  False not in self.asserts.assert_general('BIN')

    @allure.story('测试BIT_LENGTH')
    def test_BIT_LENGTH_function(self):
        assert  False not in self.asserts.assert_general('BIT_LENGTH')

    @allure.story('测试CONCAT_WS')
    def test_BIT_LENGTH_function(self):
        assert  False not in self.asserts.assert_general('CONCAT_WS')

    @allure.story('测试ELT')
    def test_ELT_function(self):
        assert  False not in self.asserts.assert_general('ELT')

    @allure.story('测试DAY')
    def test_DAY_function(self):
        assert  False not in self.asserts.assert_general('DAY')

    @allure.story('测试MONTH')
    def test_MONTH_function(self):
        assert  False not in self.asserts.assert_general('MONTH')

    @allure.story('测试YEAR')
    def test_YEAR_function(self):
        assert  False not in self.asserts.assert_general('YEAR')

    @allure.story('测试EXTRACT')
    def test_EXTRACT_function(self):
        assert  False not in self.asserts.assert_general('EXTRACT')

    @allure.story('测试ADDDATE')
    def test_ADDDATE_function(self):
        assert  False not in self.asserts.assert_general('ADDDATE')

    @allure.story('测试DATE_FORMAT')
    def test_DATE_FORMAT_function(self):
        assert  False not in self.asserts.assert_general('DATE_FORMAT')

    @allure.story('测试DATE_SUB')
    def test_DATE_SUB_function(self):
        assert  False not in self.asserts.assert_general('DATE_SUB')

    @allure.story('测试DATEDIFF')
    def test_DATEDIFF_function(self):
        assert  False not in self.asserts.assert_general('DATEDIFF')

    @allure.story('测试DAYNAME')
    def test_DAYNAME_function(self):
        assert  False not in self.asserts.assert_general('DAYNAME')

    @allure.story('测试DAYOFMONTH')
    def test_DAYOFMONTH_function(self):
        assert  False not in self.asserts.assert_general('DAYOFMONTH')

    @allure.story('测试FROM_DAYS')
    def test_FROM_DAYS_function(self):
        assert  False not in self.asserts.assert_general('FROM_DAYS')

    @allure.story('测试CONVERT')
    def test_CONVERT_function(self):
        assert  False not in self.asserts.assert_general('CONVERT')

    @allure.story('测试CAST')
    def test_CAST_function(self):
        assert  False not in self.asserts.assert_general('CAST')

    @allure.story('测试AVG')
    def test_AVG_function(self):
        assert  False not in self.asserts.assert_general('AVG')

    @allure.story('测试COUNT')
    def test_COUNT_function(self):
        assert  False not in self.asserts.assert_general('COUNT')

    @allure.story('测试SUM')
    def test_SUM_function(self):
        assert  False not in self.asserts.assert_general('SUM')

    @allure.story('测试MIN')
    def test_MIN_function(self):
        assert  False not in self.asserts.assert_general('MIN')

    @allure.story('测试MAX')
    def test_MAX_function(self):
        assert  False not in self.asserts.assert_general('MAX')

    @allure.story('测试CASE')
    def test_CASE_function(self):
        assert  False not in self.asserts.assert_general('CASE')

    @allure.story('测试IF')
    def test_IF_function(self):
        assert  False not in self.asserts.assert_general('IF')

    @allure.story('测试LIMIT')
    def test_LIMIT_function(self):
        assert  False not in self.asserts.assert_general('LIMIT')

    @allure.story('测试LIKE')
    def test_LIKE_function(self):
        assert  False not in self.asserts.assert_general('LIKE')

    @allure.story('测试IN')
    def test_IN_function(self):
        assert  False not in self.asserts.assert_general('IN')

    @allure.story('测试NOT_IN')
    def test_NOT_IN_function(self):
        assert  False not in self.asserts.assert_general('NOT_IN')

    @allure.story('测试BETWEEN_AND')
    def test_BETWEEN_AND_function(self):
        assert  False not in self.asserts.assert_general('BETWEEN_AND')

    @allure.story('测试NORMAL_JOIN')
    def test_NORMAL_JOIN_function(self):
        assert  False not in self.asserts.assert_general('NORMAL_JOIN')

    @allure.story('测试INNER_JOIN')
    def test_INNER_JOIN_function(self):
        assert  False not in self.asserts.assert_general('INNER_JOIN')

    @allure.story('测试LEFT_JOIN')
    def test_INNER_JOIN_function(self):
        assert  False not in self.asserts.assert_general('LEFT_JOIN')

    @allure.story('测试LEFT_JOIN')
    def test_LEFT_JOIN_function(self):
        assert  False not in self.asserts.assert_general('LEFT_JOIN')

    @allure.story('测试UNION')
    def test_UNION_function(self):
        assert  False not in self.asserts.assert_general('UNION')

    @allure.story('测试where_clause')
    def test_where_clause_function(self):
        assert  False not in self.asserts.assert_general('where_clause')

    @allure.story('测试DISTINCT')
    def test_DISTINCT_function(self):
        assert  False not in self.asserts.assert_general('DISTINCT')

    @allure.story('测试LONG_SQL')
    def test_LONG_SQL_function(self):
        assert  False not in self.asserts.assert_general('LONG_SQL')