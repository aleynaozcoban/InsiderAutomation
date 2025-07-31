from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    MENU_COMPANY = (By.LINK_TEXT, 'Company')
    MENU_CAREERS = (By.LINK_TEXT, 'Careers')

    def hover_menu_company(self):
        self.hover_element(*self.MENU_COMPANY) # ana sayfada yer alan menüdeki company kısmına hover yapmak için kullanılan fonksiyondur


    def click_menu_careers(self):
        self.click_element(*self.MENU_CAREERS) # company kısmına hover yaptıktan sonra açılan menüde careers bağlantısına tıklar
