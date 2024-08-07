import time
from Tests.Base import BaseTest
from Pages.LandingPage import LandingPage
from Utils.Utilities import find_nth_true
import random


class LandingPageTest(BaseTest):
    def test_ludo_startup(self):
        landing_page = LandingPage(self.driver, self.wait, self.actions)
        landing_page.click_play_as_guest()
        landing_page.click_continue_button()
        landing_page.click_play_with_computer()
        landing_page.click_next_button()
        landing_page.click_play_button()

    def test_ludo(self):
        landing_page = LandingPage(self.driver, self.wait, self.actions)
        landing_page.click_play_as_guest()
        landing_page.click_continue_button()
        landing_page.click_play_with_computer()
        landing_page.click_next_button()
        landing_page.click_play_button()

        index = 0  # track which pieces are playing the game
        element_status = [False] * 4  # True if the piece has come into the play
        for i in range(5):
            if index < 4 and landing_page.is_dice_6():
                landing_page.tap_on_piece_by_index(index)
                element_status[index] = True
                index += 1
                landing_page.tap_on_dice()
            elif index == 1:
                landing_page.tap_on_dice()
            else:
                random_index = random.randint(0, index if index == 0 else index - 1)
                landing_page.tap_on_piece_by_index(find_nth_true(element_status, random_index))
                landing_page.tap_on_dice()
