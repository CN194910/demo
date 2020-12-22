#!/usr/bin/python3

import time
import logging
from logging import handlers
from demo.utils.common_utils import CommonUtils

class Logger(object):
    def __init__(self, logger_name):
        
        #创建logger及输入名称
        self.logger = logging.getLogger(logger_name)
        #设置日志等级
        self.logger.setLevel(logging.DEBUG)
        
        #设置日志名称及路径
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        log_path = CommonUtils.make_direction('log')
        log_file_name = CommonUtils.get_file_path(log_path, rq+'.log')
        
        #创建文件handler并以天进行日志分割
        #fh = handlers.TimedRotatingFileHandler(filename=log_file_name, when='D', backupCount=3, encoding='utf-8')
        fh = logging.FileHandler(log_file_name, encoding='utf-8')
        #创建控制台handler
        ch = logging.StreamHandler()
        
        #日志输入格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        
    def get_logger(self):
        return self.logger
        
        
if __name__ == '__main__':
    logger = Logger('test').get_logger()
    while True:
        time.sleep(0.5)
        logger.debug('debug')
        logger.info('info')