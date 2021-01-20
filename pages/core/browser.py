from selenium import webdriver
import demo.conf.settings as s
from demo.utils.logger import Logger

logger = Logger('BrowserEngine').get_logger()

class BrowserEngine(object):
    def __init__(self, url=None):
        self.driver = self.__init_browser()
        self.root_url = s.root_url + url if url else s.root_url

    def __init_browser(self):
        cb = s.chose_browser
        if cb == 'firefox':
            driver = webdriver.Firefox(executable_path=s.linux_firefox_driver)
            logger.info('火狐游览器已启动')
        elif cb == 'chrome':
            driver = webdriver.Chrome(executable_path=s.linux_chrome_driver)
            logger.info('谷歌游览器已启动')
        else:
            driver = s.default_browser(executable_path=s.linux_firefox_driver) 
            logger.info('火狐游览器已启动')
        return driver

    def open_browser(self):
        self.driver.get(self.root_url)
        logger.info('打开网址: {}'.format(self.root_url))
        self.driver.maximize_window()
        logger.info('游览器窗口最大化')
        self.driver.implicitly_wait(s.implicit_timeout)
        logger.info('implicitly_wait: {}'.format(s.implicit_timeout))

    def quit_browser(self):
        self.driver.quit()
        logger.info('关闭游览器')

if __name__ == '__main__':
    BrowserEngine(r'?from=M126_LOGIN').open_browser()

