from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, wait, actions=None):
        self.driver = driver
        self.wait = wait
        self.actions = actions

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_element_by_accessibility_id(self, accessibility_id):
        return self.wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, accessibility_id)))

    def find_element_by_id(self, element_id):
        return self.wait.until(EC.presence_of_element_located((AppiumBy.ID, element_id)))

    def find_element_by_xpath(self, xpath):
        return self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, xpath)))

    def find_element_by_image(self, image, wait=None):
        if wait:
            return wait.until(EC.presence_of_element_located((AppiumBy.IMAGE, image)))
        return self.wait.until(EC.presence_of_element_located((AppiumBy.IMAGE, image)))

    def is_element_exist(self, by, value):
        try:
            self.driver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False

    def is_image_element_exist(self, wait, value):
        try:
            wait.until(EC.presence_of_element_located((AppiumBy.IMAGE, value)))
            return True
        except NoSuchElementException:
            return False
