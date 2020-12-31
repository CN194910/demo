from selenium.webdriver import Firefox
from demo.utils.common_utils import CommonUtils as cu


#地址
root_url = 'https://mail.126.com/'

#超时时间
wait_timeout = 5
implicit_timeout = 5

#游览器
default_driver = Firefox
firefox_path = cu.get_file_path(cu.make_direction('tools'), 'geckodriver.exe')
chrome_path = cu.get_file_path(cu.make_direction('tools'), 'chromedriver.exe')
