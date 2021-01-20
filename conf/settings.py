from selenium.webdriver import Firefox
from demo.utils.common_utils import CommonUtils as cu


#地址
root_url = 'https://mail.126.com/'

#超时时间
wait_timeout = 5
implicit_timeout = 5

#游览器
default_browser = Firefox
chose_browser = 'firefox'
linux_firefox_driver = cu.get_file_path(cu.make_direction('tools'), 'geckodriver')
linux__chrome_driver = cu.get_file_path(cu.make_direction('tools'), 'chromedriver')
win_firefox_driver = cu.get_file_path(cu.make_direction('tools'), 'geckodriver.exe')
win__chrome_driver = cu.get_file_path(cu.make_direction('tools'), 'chromedriver.exe')
