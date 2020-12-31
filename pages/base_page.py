import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import demo.conf.settings as s
from demo.utils.common_utils import CommonUtils
from demo.utils.logger import Logger

logger = Logger('BasePage').get_logger()


class BasePage(object):
    def __init__(self, driver, bases_url=None):
        self.driver = driver
        self.root_url = bases_url if bases_url else s.root_url
        
    def open(self, url=None):
        url = self.root_url + url
        self.driver.get(url)
        self.implicitly_wait(s.implicit_timeout)
        logger.info('启动游览器，打开网址: '.format(url))

    def get_windows_img(self):
        screenshots_path = CommonUtils.make_direction('screenshots')
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screenshots_name  = CommonUtils.get_file_path(screenshots_path, rq+'.png')
        self.driver.get_screenshot_as_file(screenshots_name)
        logger.info("截图文件: {}".format(screenshots_name))

    def find_element(self, *locator):
        try:
            is_displayed = WebDriverWait(self.driver, s.wait_timeout).until(EC.visibility_of_element_located(locator))
            if is_displayed:
                self.driver.find_element(*locator)
                logger.info('已找到元素: {}'.format(locator))
        except TimeoutException:
            logger.error("在给定的时间{}内，元素未找到: {}".format(s.wait_timeout, locator[1]))
            self.get_windows_img()
        
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_title(self):
        longger.info('当前页面标题是：{}'.format(self.driver.title))
        return self.driver.title

    def get_url(self):
        longger.info('当前页面URL是：{}'.format(self.driver.current_url))
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()


if __name__ == '__main__':
    BasePage()
