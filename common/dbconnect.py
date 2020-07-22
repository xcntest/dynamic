# -*- coding:utf-8 -*-
'''
@Time       : 2020/6/30 19:35
@Author     : Joy
@FileName   : dbconnect.py
'''

import pymysql
from common import readfiles
from tools import filetools

class DBOperate:
    #获取连接
    #def connectdb(conninfo):
    def __init__(self,conninfo):
        self.conninfo = conninfo
        try:
            self.conn = pymysql.connect(
                                    host = self.conninfo.host,
                                    port = self.conninfo.port,
                                    db = self.conninfo.dbname,
                                    user = self.conninfo.user,
                                    passwd = conninfo.pwd,
                                    charset = 'utf8')
            print("连接成功")
        except Exception as e:
            print("连接失败，失败原因为{}".format(e))


    #封装更改数据库操作
    def quey_db(self,sqlinfo):
        """
        :param sqlinfo:sql yaml
        :return: 查询元组
        """
        #获取连接
        print(sqlinfo.sql)
        with self.conn as cursor:
            with cursor:
                try:
                    cursor.execute(sqlinfo.sql) #执行sql
                    result = cursor.fetchall() #获取所有查询结果
                except Exception as e:
                    print("{}查询失败，原因{}".format(sqlinfo.sql,e))
        self.conn.close()
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
    conninfo = readfiles.read_yaml('common/config.yaml')
    db = DBOperate(conninfo)

    # 获取配置信息
    # conndata = readfiles.read_yaml('common/config.yaml')
    # conninfo = filetools.AttrDict(conndata['mysql'])
    # sqlfile = readfiles.read_yaml('sqlfiles/mysqlsql/DQL.yaml')
    # sqlinfo = filetools.AttrDict(sqlfile['mysqldql'][0])
    # quey_db(conninfo,sqlinfo)





