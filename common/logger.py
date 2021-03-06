# -*- coding:utf-8 -*-
'''
@Time       : 2020/8/5 14:03
@Author     : Joy
@FileName   : logger.py
'''

# -*- coding: utf-8 -*-
import os
import time
from logging.handlers import RotatingFileHandler
import logging
from tools import makedir
import inspect

#获取当前文件的根目录，再拼接Log路径
dir = os.path.join(os.path.split(os.path.dirname(__file__))[0],'Logs')
#没有logs创建logs文件夹
makedir.mk_dir(dir)

handlers = {#logging.NOTSET: os.path.join(dir, 'notset.txt'),

            logging.DEBUG: os.path.join(dir, 'debug.log'),

            logging.INFO: os.path.join(dir, 'info.log'),

            #logging.WARNING: os.path.join(dir, 'warning.txt'),

            logging.ERROR: os.path.join(dir, 'error.log'),

            #logging.CRITICAL: os.path.join(dir, 'critical.txt'),
            }


def createHandlers():
    logLevels = handlers.keys()

    for level in logLevels:
        path = os.path.abspath(handlers[level])
        #这里定义写入日志的方法，覆盖写还是追加写
        handlers[level] = RotatingFileHandler(path, maxBytes=10000, backupCount=2, encoding='GBK')
        # handlers[level] = logging.FileHandler(path)


# 加载模块时创建全局变量

createHandlers()


class Log(object):

    def printfNow(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def __init__(self, level=logging.NOTSET):
        self.__loggers = {}

        logLevels = handlers.keys()

        for level in logLevels:
            logger = logging.getLogger(str(level))

            # 如果不指定level，获得的handler似乎是同一个handler?

            logger.addHandler(handlers[level])

            logger.setLevel(level)

            self.__loggers.update({level: logger})

    def getLogMessage(self, level, message):
        frame, filename, lineNo, functionName, code, unknowField = inspect.stack()[2]

        '''日志格式：[时间] [类型] [记录代码] 信息'''

        return "[%s] [%s] [%s-%s - %s] %s" % (self.printfNow(), level, filename,lineNo, functionName, message)

    def info(self, message):
        message = self.getLogMessage("info", message)

        self.__loggers[logging.INFO].info(message)

    def error(self, message):
        message = self.getLogMessage("error", message)

        self.__loggers[logging.ERROR].error(message)

    # def warning(self, message):
    #     message = self.getLogMessage("warning", message)
    #
    #     self.__loggers[logging.WARNING].warning(message)

    def debug(self, message):
        message = self.getLogMessage("debug", message)

        self.__loggers[logging.DEBUG].debug(message)

    # def critical(self, message):
    #     message = self.getLogMessage("critical", message)
    #
    #     self.__loggers[logging.CRITICAL].critical(message)


if __name__ == "__main__":
    logger = Log()
    logger.debug("debug")
    logger.info("info")
    logger.error("error")
