#!/usr/bin/python3

import sys
import logging
from demo.utils.common_utils import CommonUtils

class Logger(object):
    log_path = CommonUtils.make_direction('log')
    
if __name__ == '__main__':
    logger = Logger()
