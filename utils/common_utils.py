#! /usr/bin/python3

import os
import time
import datetime
#from demo.utils.logger import Logger


class CommonUtils(object):

    @staticmethod
    def get_project_path():
        file_path = os.path.dirname(os.path.abspath(__file__))
        project_path = os.path.dirname(file_path)
        return project_path
    
    @staticmethod
    def make_direction(path):
        path = path.strip()
        new_path = os.path.join(CommonUtils.get_project_path(), path)
        if not os.path.exists(new_path):
            os.mkdir(new_path)
        return new_path
    
    @staticmethod
    def get_file_path(path, filename):
        return os.path.join(path, filename)
'''            
    @staticmethod
    def delete_files(path, offset):
        logger = Logger('delete_files').get_logger()
        #获取当前时间
        current_time = datetime.datetime.now()
        #设置时间偏移量
        time_offset = datetime.timedelta(days=-offset)
        #获取想要的日期
        re_date = (current_time + time_offset)
        #将时间转换成时间戳
        re_date_unix = time.mktime(re_date.timetuple())
        logger.info('删除{}目录下,{}天前的文件'.format(path, offset))
        
        #递归遍历给定的路径
        for root, dirs, files in os.walk(path):
            for file in files:
                #拼接路径和文件
                filename = os.path.join(root, file)
                #获取文件修改时间（时间戳）
                file_mtime = os.path.getmtime(filename)
                #把时间转换为人类可读时间
                timeArray = time.localtime(file_time)
                human_readable_time = time.strftime('%Y%m%d%H%M%S', timeArray)
                
                if file_mtime <= re_date_unix:
                    #删除文件
                    os.remove(filename)
                    logger.info('删除文件: {},文件修改时间: {}'.format(filename, human_readable_time))
'''

if __name__ == '__main__':
    import time
    print(CommonUtils.get_project_path())
    log_path = CommonUtils.make_direction('log')
    rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    print(CommonUtils.get_file_path(rq+'.log', log_path))
