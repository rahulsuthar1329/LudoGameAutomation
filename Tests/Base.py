import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.action_chains import ActionChains

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='e498fd29',
    appPackage='com.vinaykpro.ludoking',
    appActivity='com.vinaykpro.ludoking.HomeActivity',
    enableMultiWindows=True
)

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)


class BaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)
        self.wait = WebDriverWait(self.driver, 15)
        self.actions = ActionChains(self.driver, duration=5000)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
