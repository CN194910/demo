import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from demo.utils.common_utils import CommonUtils
from demo.utils.logger import Logger


logger = Logger('BasePage').get_logger()


class BasePage(object):
    def __init__(self, driver, timeout=10, base_url='https://mail.126.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = timeout

    def get_windows_img(self):
        screenshots_path = CommonUtils.make_direction('screenshots')
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screenshots_name  = CommonUtils.get_file_path(screenshots_path, rq+'.png')
        self.driver.get_screenshot_as_file(screenshots_name)
        logger.info("截图文件: {}".format(locator, screenshots_name))

    def find_element(self, *locator):
        try:
            element = self.driver.find_element(*locator)
            logger.info('已找到元素: {}'.format(locator))
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: {}".format(e))
            self.get_windows_img()
        
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def open(self, url=None):
        url = self.base_url + url
        self.driver.get(url)
        logger.info('启动游览器，打开网址: '.format(url))

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()

if __name__ == '__main__':
    BasePage()
