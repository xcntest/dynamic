import allure
from dbopration import mysqlconn
from common import readfiles,asserts

@allure.feature("mysql∫Ø ˝≤‚ ‘")
class TestAllTypes:

    def setup_class(self):
        # ªÒ»° ˝æ›ø‚¡¨Ω”∂‘œÛ
        self.conninfo = readfiles.read_yaml('dbopration\config.yaml','mysql')
        self.dbconn = mysqlconn.DBOperate(self.conninfo)
        self.sqlpath = 'sqlfiles\mysqlsql\other_select.yaml'
        self.asserts = asserts.Pro_Result(self.sqlpath,self.dbconn)

    def teardown_class(self):
        self.dbconn.conn.close()

    @allure.story('≤‚ ‘ABS')
    def test_abs_function(self):
        assert  False not in self.asserts.assert_general('ABS')

    @allure.story('≤‚ ‘MOD')
    def test_ABS_function(self):
        assert  False not in self.asserts.assert_general('MOD')

    @allure.story('≤‚ ‘CEILING')
    def test_CEILING_function(self):
        assert  False not in self.asserts.assert_general('CEILING')

    @allure.story('≤‚ ‘ROUND')
    def test_ROUND_function(self):
        assert  False not in self.asserts.assert_general('ROUND')

    @allure.story('≤‚ ‘POW')
    def test_POW_function(self):
        assert  False not in self.asserts.assert_general('POW')

    @allure.story('≤‚ ‘POWER')
    def test_POWER_function(self):
        assert  False not in self.asserts.assert_general('POWER')

    @allure.story('≤‚ ‘FLOOR')
    def test_FLOOR_function(self):
        assert  False not in self.asserts.assert_general('FLOOR')

    @allure.story('≤‚ ‘RAND')
    def test_RAND_function(self):
        assert  False not in self.asserts.assert_general('RAND')

    @allure.story('≤‚ ‘ASCII')
    def test_ASCII_function(self):
        assert  False not in self.asserts.assert_general('ASCII')

    @allure.story('≤‚ ‘CONCAT')
    def test_CONCAT_function(self):
        assert  False not in self.asserts.assert_general('CONCAT')

    @allure.story('≤‚ ‘LENGTH')
    def test_LENGTH_function(self):
        assert  False not in self.asserts.assert_general('LENGTH')

    @allure.story('≤‚ ‘LOCATE')
    def test_LOCATE_function(self):
        assert  False not in self.asserts.assert_general('LOCATE')

    @allure.story('≤‚ ‘INSTR')
    def test_INSTR_function(self):
        assert  False not in self.asserts.assert_general('INSTR')

    @allure.story('≤‚ ‘LEFT')
    def test_LEFT_function(self):
        assert  False not in self.asserts.assert_general('LEFT')

    @allure.story('≤‚ ‘RIGHT')
    def test_RIGHT_function(self):
        assert  False not in self.asserts.assert_general('RIGHT')

    @allure.story('≤‚ ‘SUBSTRING')
    def test_SUBSTRING_function(self):
        assert  False not in self.asserts.assert_general('SUBSTRING')

    @allure.story('≤‚ ‘REPEAT')
    def test_REPEAT_function(self):
        assert  False not in self.asserts.assert_general('REPEAT')

    @allure.story('≤‚ ‘REVERSE')
    def test_REVERSE_function(self):
        assert  False not in self.asserts.assert_general('REVERSE')

    @allure.story('≤‚ ‘INSERT')
    def test_INSERT_function(self):
        assert  False not in self.asserts.assert_general('INSERT')

    @allure.story('≤‚ ‘LOWER')
    def test_LOWER_function(self):
        assert  False not in self.asserts.assert_general('LOWER')

    @allure.story('≤‚ ‘UPPER')
    def test_UPPER_function(self):
        assert  False not in self.asserts.assert_general('UPPER')

    @allure.story('≤‚ ‘BIN')
    def test_BIN_function(self):
        assert  False not in self.asserts.assert_general('BIN')

    @allure.story('≤‚ ‘BIT_LENGTH')
    def test_BIT_LENGTH_function(self):
        assert  False not in self.asserts.assert_general('BIT_LENGTH')

    @allure.story('≤‚ ‘CONCAT_WS')
    def test_BIT_LENGTH_function(self):
        assert  False not in self.asserts.assert_general('CONCAT_WS')

    @allure.story('≤‚ ‘ELT')
    def test_ELT_function(self):
        assert  False not in self.asserts.assert_general('ELT')

    @allure.story('≤‚ ‘DAY')
    def test_DAY_function(self):
        assert  False not in self.asserts.assert_general('DAY')

    @allure.story('≤‚ ‘MONTH')
    def test_MONTH_function(self):
        assert  False not in self.asserts.assert_general('MONTH')

    @allure.story('≤‚ ‘YEAR')
    def test_YEAR_function(self):
        assert  False not in self.asserts.assert_general('YEAR')

    @allure.story('≤‚ ‘EXTRACT')
    def test_EXTRACT_function(self):
        assert  False not in self.asserts.assert_general('EXTRACT')

    @allure.story('≤‚ ‘ADDDATE')
    def test_ADDDATE_function(self):
        assert  False not in self.asserts.assert_general('ADDDATE')

    @allure.story('≤‚ ‘DATE_FORMAT')
    def test_DATE_FORMAT_function(self):
        assert  False not in self.asserts.assert_general('DATE_FORMAT')

    @allure.story('≤‚ ‘DATE_SUB')
    def test_DATE_SUB_function(self):
        assert  False not in self.asserts.assert_general('DATE_SUB')

    @allure.story('≤‚ ‘DATEDIFF')
    def test_DATEDIFF_function(self):
        assert  False not in self.asserts.assert_general('DATEDIFF')

    @allure.story('≤‚ ‘DAYNAME')
    def test_DAYNAME_function(self):
        assert  False not in self.asserts.assert_general('DAYNAME')

    @allure.story('≤‚ ‘DAYOFMONTH')
    def test_DAYOFMONTH_function(self):
        assert  False not in self.asserts.assert_general('DAYOFMONTH')

    @allure.story('≤‚ ‘FROM_DAYS')
    def test_FROM_DAYS_function(self):
        assert  False not in self.asserts.assert_general('FROM_DAYS')

    @allure.story('≤‚ ‘CONVERT')
    def test_CONVERT_function(self):
        assert  False not in self.asserts.assert_general('CONVERT')

    @allure.story('≤‚ ‘CAST')
    def test_CAST_function(self):
        assert  False not in self.asserts.assert_general('CAST')

    @allure.story('≤‚ ‘AVG')
    def test_AVG_function(self):
        assert  False not in self.asserts.assert_general('AVG')

    @allure.story('≤‚ ‘COUNT')
    def test_COUNT_function(self):
        assert  False not in self.asserts.assert_general('COUNT')

    @allure.story('≤‚ ‘SUM')
    def test_SUM_function(self):
        assert  False not in self.asserts.assert_general('SUM')

    @allure.story('≤‚ ‘MIN')
    def test_MIN_function(self):
        assert  False not in self.asserts.assert_general('MIN')

    @allure.story('≤‚ ‘MAX')
    def test_MAX_function(self):
        assert  False not in self.asserts.assert_general('MAX')

    @allure.story('≤‚ ‘CASE')
    def test_CASE_function(self):
        assert  False not in self.asserts.assert_general('CASE')

    @allure.story('≤‚ ‘IF')
    def test_IF_function(self):
        assert  False not in self.asserts.assert_general('IF')

    @allure.story('≤‚ ‘LIMIT')
    def test_LIMIT_function(self):
        assert  False not in self.asserts.assert_general('LIMIT')

    @allure.story('≤‚ ‘LIKE')
    def test_LIKE_function(self):
        assert  False not in self.asserts.assert_general('LIKE')

    @allure.story('≤‚ ‘IN')
    def test_IN_function(self):
        assert  False not in self.asserts.assert_general('IN')

    @allure.story('≤‚ ‘NOT_IN')
    def test_NOT_IN_function(self):
        assert  False not in self.asserts.assert_general('NOT_IN')

    @allure.story('≤‚ ‘BETWEEN_AND')
    def test_BETWEEN_AND_function(self):
        assert  False not in self.asserts.assert_general('BETWEEN_AND')

    @allure.story('≤‚ ‘NORMAL_JOIN')
    def test_NORMAL_JOIN_function(self):
        assert  False not in self.asserts.assert_general('NORMAL_JOIN')

    @allure.story('≤‚ ‘INNER_JOIN')
    def test_INNER_JOIN_function(self):
        assert  False not in self.asserts.assert_general('INNER_JOIN')

    @allure.story('≤‚ ‘LEFT_JOIN')
    def test_INNER_JOIN_function(self):
        assert  False not in self.asserts.assert_general('LEFT_JOIN')

    @allure.story('≤‚ ‘LEFT_JOIN')
    def test_LEFT_JOIN_function(self):
        assert  False not in self.asserts.assert_general('LEFT_JOIN')

    @allure.story('≤‚ ‘UNION')
    def test_UNION_function(self):
        assert  False not in self.asserts.assert_general('UNION')

    @allure.story('≤‚ ‘where_clause')
    def test_where_clause_function(self):
        assert  False not in self.asserts.assert_general('where_clause')

    @allure.story('≤‚ ‘DISTINCT')
    def test_DISTINCT_function(self):
        assert  False not in self.asserts.assert_general('DISTINCT')

    @allure.story('≤‚ ‘LONG_SQL')
    def test_LONG_SQL_function(self):
        assert  False not in self.asserts.assert_general('LONG_SQL')