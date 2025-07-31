from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DepartmentPage(BasePage):
    QA_JOBS = (By.LINK_TEXT, 'See all QA jobs')

    def click_job(self):
        self.click_element(*self.QA_JOBS) # See all QA jobs butonuna tıklar

