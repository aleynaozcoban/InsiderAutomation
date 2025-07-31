from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CareersPage(BasePage):
    LOCATIONS_BLOCK = (By.ID, 'career-our-location')
    TEAMS_BLOCK = (By.ID, 'career-find-our-calling')
    LIFE_AT_INSIDER_BLOCK = (By.XPATH,
                             "//h2[contains(text(), 'Life at Insider')]/ancestor::section")


    def is_block_visible(self):
        # Kariyer sayfasında teams, location, life at insider bloklarının görünüp görünmediğini kontrol eder
        locations = self.find(*self.LOCATIONS_BLOCK).is_displayed()
        teams = self.find(*self.TEAMS_BLOCK).is_displayed()
        life_at_insider = self.find(*self.LIFE_AT_INSIDER_BLOCK).is_displayed()
        return locations and teams and life_at_insider

