import time
import sys
print(sys.path)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from demo.utils.common_utils import CommonUtils
from demo.utils.logger import Logger

# this Base class is serving basic attributes for every single page inherited from Page class
class BasePage(object):
    def __init__(self, driver, timeout=10, base_url='https://mail.126.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = timeout
        Logger()
        
    def get_windows_img(self):
        screenshots_path = CommonUtils.make_direction('screenshots')
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screenshots_name  = rq + '.png'
        self.driver.get_screenshot_as_file(CommonUtils.get_file_path(screenshots_name, screenshots_path))

    def find_element(self, *locator):
        return self.driver.find_element(*locator)
        
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

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
