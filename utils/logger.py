#!/usr/bin/python3

import time
import logging
from demo.utils.common_utils import CommonUtils

class Logger(object):
    def __init__(self, logger_name):
        
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        
        rq = time.strftime('%Y%m%d%H%M%S', time.asctime(time.time()))
        log_path = CommonUtils.make_direction('log')
        
        
        fh = logging.FileHanadler("")
        
if __name__ == '__main__':
    logger = Logger()
