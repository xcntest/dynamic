# -*- coding:utf-8 -*-
'''
@Time       : 2020/6/30 19:35
@Author     : Joy
@FileName   : mysqlconn.py
'''

import pymysql
from common import readfiles
from tools import filetools
from common import logger

class DBOperate:
    #获取连接
    #def connectdb(conninfo):
    def __init__(self,conninfo):
        self.logger = logger.Log()
        self.conninfo = conninfo
        try:
            self.conn = pymysql.connect(
                                    host = self.conninfo.host,
                                    port = self.conninfo.port,
                                    db = self.conninfo.dbname,
                                    user = self.conninfo.user,
                                    passwd = conninfo.pwd,
                                    charset = 'utf8')
            self.logger.info("连接成功")
        except Exception as e:
            self.logger.error("连接失败，失败原因为{}".format(e))


    #封装查询数据库操作
    def quey_db(self,sqlinfo):
        """
        :param sqlinfo:sql yaml
        :return: 查询元组
        """
        # 判断SQL是否为字段类型查询，如果是，则不带列名，如果不是，则带列名
        # 注：此方法要求sql文件内的casename一定要存在
        if sqlinfo.casename == 'coltype':
            with self.conn as cursor:
                with cursor:
                    try:
                        cursor.execute(sqlinfo.sql) #执行sql
                        result = dict(cursor.fetchall())#获取所有查询结果
                    except Exception as e:
                        self.logger.error("{}查询失败，原因{}".format(sqlinfo.sql,e))
        else:
            with self.conn.cursor(pymysql.cursors.DictCursor)  as cursor:
                with cursor:
                    try:
                        cursor.execute(sqlinfo.sql) #执行sql
                        result = cursor.fetchall()#获取所有查询结果
                    except Exception as e:
                        self.logger.error("{}查询失败，原因{}".format(sqlinfo.sql,e))
        return result


    #修改数据库操作
    def  alter_db(self,sql):
        """
        :param sql:
        :return:
        """
        with self.conn as cursor:
            #cursor上下文本有异常回滚操作
            with cursor:
                try:
                    cursor.execute(sql) #执行sql
                except Exception as e:
                    print("{}修改失败，原因{}".format(sql,e))
        self.conn.close()




if __name__ == '__main__':
    conninfo = readfiles.read_yaml('dbopration/config.yaml','mysql')
    db = DBOperate(conninfo)
    # sql = readfiles.read_yaml('sqlfiles/mysqlsql/mask_all_types.yaml','coltype')
    # result = db.quey_db(sql)
    sql = readfiles.read_yaml('sqlfiles/mysqlsql/mask_all_types.yaml','alltypes')
    result2 = db.quey_db(sql)[0]
    print(result2)
    print(str(result2['COL_24_date']))
    print(str(result2['COL_25_time']))
    print(str(result2['COL_26_datetime']))
    print(str(result2['COL_27_year']))
    print(str(result2['COL_28_timestamp']))
    db.conn.close()









