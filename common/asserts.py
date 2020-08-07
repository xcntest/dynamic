# -*- coding:utf-8 -*-
'''
@Time       : 2020/8/6 18:18
@Author     : Joy
@FileName   : asserts.py
'''

from common import readfiles,logger
import allure

class Pro_Result():

    def __init__(self, sqlpath,dbconn):
        """
        :param connpath: 数据库信息配置文件路径
        :param connsection: 数据库类型section
        :param sqlpath: sql文件存放路径
        """
        # 获取数据库连接对象
        # self.conninfo = readfiles.read_yaml(connpath, connsection)
        # self.dbconn = mysqlconn.DBOperate(self.conninfo)
        self.dbconn = dbconn
        self.sqlpath = sqlpath
        self.strlist = ['char', 'varchar', 'binary', 'varbinary', 'enum', 'set']
        self.numlist = ['int', 'interger', 'tinyint', 'smallint', 'mediumint', 'bigint', 'serial']
        self.datelist = ['date', 'year', 'timestamp','time','datatime']
        self.floatlist = ['numeric', 'decimal']
        self.otherlist = ['tinyblob', 'blob', 'mediumblob', 'longtext', 'bit']
        self.logger = logger.Log()

    # 获取测试用例表格的字段名及字段类型数据类型
    def get_col_type(self, section='coltype'):
        """
        :param section: 一般为coltype
        :return: 返回表类型及字段名
        """
        sql = readfiles.read_yaml(self.sqlpath, section)
        typedict = self.dbconn.quey_db(sql)
        return typedict

    # 处理获取到具体查询数据
    def get_col_value(self, section):
        """
        :param section: sql yaml中的section
        :return: 表字段名及内容，为带字典的列表
        """
        sql = readfiles.read_yaml(self.sqlpath, section)
        valuedict = self.dbconn.quey_db(sql)
        return valuedict


    def assert_result(self,valuesection,typesection='coltype'):
        #定义结果集
        resultlist = []
        # 获取列表和列类型字典
        coltype = self.get_col_value(typesection)
        # 获取数据
        data = self.get_col_type(valuesection)[0]
        # 处理获取到的数据
        for k, v in data.items():
            if coltype[k] in self.strlist:
                if '*' in str(v):
                    result = True
                else:
                    result = False

                    #加入allure false内容输入出
                    with allure.step("日期类型错误字段"):
                        allure.attach("脱敏错误数据类型为", str(k))
                        allure.attach("值为", str(v))

                    self.logger.info('失败的字段为{}值为{}'.format(k, v))
            elif coltype[k] in self.numlist:
                if '108' or '10' or '1' in str(v):
                    result = True
                else:
                    result = False

                    #加入allure false内容输入出
                    with allure.step("日期类型错误字段"):
                        allure.attach("脱敏错误数据类型为", str(k))
                        allure.attach("值为", str(v))

                    self.logger.info('失败的字段为{}值为{}'.format(k, v))
            elif coltype[k] in self.datelist:
                if '1970-01-01' in str(v):
                    result = True
                else:
                    result = False
                    #加入allure false内容输入出
                    with allure.step("日期类型错误字段"):
                        allure.attach("脱敏错误数据类型娄", str(k))
                        allure.attach("值为", str(v))

                    self.logger.info('失败的字段为{}值为{}'.format(k, v))
            elif coltype[k] in self.floatlist:
                if '0.8' or '8.8' or '.8' in str(v):
                    result = True
                else:
                    result = False
                    #加入allure false内容输入出
                    with allure.step("日期类型错误字段"):
                        allure.attach("脱敏错误数据类型娄", str(k))
                        allure.attach("值为", str(v))

                    self.logger.info('失败的字段为{}值为{}'.format(k, v))
            elif coltype[k] in self.otherlist:
                if 'None' in str(v):
                    result = True
                else:
                    result = False
                    #加入allure false内容输入出
                    with allure.step("日期类型错误字段"):
                        allure.attach("脱敏错误数据类型娄", str(k))
                        allure.attach("值为", str(v))

                    self.logger.info('失败的字段为{}值为{}'.format(k,v))

            resultlist.append(result)
        print(resultlist)
        return resultlist


if __name__ == '__main__':
    proresult = Pro_Result()
    proresult.assert_result('charcheck')
