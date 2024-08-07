import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from Pages.BasePage import BasePage
from Utils.Utilities import convert_image_to_base64


class LandingPage(BasePage):
    play_as_guest_id = 'com.vinaykpro.ludoking:id/imageView25'
    continue_button_id = 'com.vinaykpro.ludoking:id/imageView46'
    play_with_computer_id = 'com.vinaykpro.ludoking:id/imageView4'
    next_button_id = 'com.vinaykpro.ludoking:id/computernxtbtn'
    play_button_id = 'com.vinaykpro.ludoking:id/computermainplaybtn'
    hint_arrow_id = 'com.vinaykpro.ludoking:id/hintarrowleft'
    piece_1 = 'com.vinaykpro.ludoking:id/imageView41'
    piece_2 = 'com.vinaykpro.ludoking:id/imageView42'
    piece_3 = 'com.vinaykpro.ludoking:id/imageView43'
    piece_4 = 'com.vinaykpro.ludoking:id/imageView44'

    play_with_friend_xpath = '//android.widget.TextView[@text="Local"]'
    dice_xpath = '//android.widget.FrameLayout[@resource-id="android:id/content"]//android.view.View[last()-1]'

    def __init__(self, driver, wait, actions):
        super().__init__(driver, wait, actions)

    def click_play_as_guest(self):
        # self.tap_on_coordinates(550, 1600)
        # self.find_element_by_id(self.play_as_guest_id).click()
        self.find_element_by_image(convert_image_to_base64("../Images/guest.jpg")).click()

    def click_continue_button(self):
        # self.tap_on_coordinates(550, 1960)
        # self.find_element_by_id(self.continue_button_id).click()
        self.find_element_by_image(convert_image_to_base64("../Images/continue.jpg")).click()

    def click_play_with_computer(self):
        # self.tap_on_coordinates(350, 1550)
        # self.find_element_by_id(self.play_with_computer_id).click()
        self.find_element_by_image(convert_image_to_base64("../Images/play_computer.jpg")).click()

    def click_next_button(self):
        # self.tap_on_coordinates(550, 1630)
        # self.find_element_by_id(self.next_button_id).click()
        self.find_element_by_image(convert_image_to_base64("../Images/next.jpg")).click()

    def click_play_button(self):
        # self.tap_on_coordinates(550, 1900)
        # self.find_element_by_id(self.play_button_id).click()
        self.find_element_by_image(convert_image_to_base64("../Images/play.jpg")).click()

    def check_if_arrow_exist(self):
        if self.is_element_exist(AppiumBy.ID, self.hint_arrow_id):
            return True
        return False

    def get_dice_1(self):
        return self.find_element_by_image(convert_image_to_base64("../Images/dice1.png"))

    def is_dice_6(self):
        return self.is_image_element_exist(WebDriverWait(self.driver, 5),
                                           convert_image_to_base64("../Images/dice6.png"))

    def tap_on_dice(self):
        self.tap_on_coordinates(250, 1930)
        time.sleep(2)

    def tap_on_first_piece(self):
        self.find_element_by_id(self.piece_1).click()

    def tap_on_second_piece(self):
        self.find_element_by_id(self.piece_2).click()

    def tap_on_third_piece(self):
        self.find_element_by_id(self.piece_3).click()

    def tap_on_fourth_piece(self):
        self.find_element_by_id(self.piece_4).click()

    def tap_on_piece_by_index(self, index):
        if index == 0:
            self.tap_on_first_piece()
        elif index == 1:
            self.tap_on_second_piece()
        elif index == 2:
            self.tap_on_third_piece()
        else:
            self.tap_on_fourth_piece()

    def tap_on_coordinates(self, x, y):
        self.driver.tap([(x, y)])
