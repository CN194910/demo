#! /usr/bin/python3

import os


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
    def get_file_path(path=None, filename):
        if path == None and filename:
            return filename
        elif filename:
            return os.path.join(path, filename)


if __name__ == '__main__':
    import time
    print(CommonUtils.get_project_path())
    log_path = CommonUtils.make_direction('log')
    rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    print(CommonUtils.get_file_path(rq+'.log', log_path))
