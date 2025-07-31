from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def close_cookie_banner(self):
            try:
                # Banner görünürse ve kabul butonu aktifse tıkla
                accept_button = self.wait_element((By.ID, "wt-cli-accept-all-btn"))
                accept_button.click()

                self.wait.until(EC.invisibility_of_element_located((By.ID, "cookie-law-info-bar")))
            except Exception:
                # Banner yoksa ya da hata olursa atla
                pass

    def find(self, *locator):
      return self.driver.find_element(*locator)

    def find_all(self, *locator):
        return self.driver.find_elements(*locator)

    def click_element(self, *locator):
      self.driver.find_element(*locator).click()

    def hover_element(self, *locator):
     element = self.find(*locator)
     hover = ActionChains(self.driver).move_to_element(element)
     hover.perform()

    def get_current_url(self):
      return self.driver.current_url


    def wait_element(self, method, message=''):
      return self.wait.until(EC.element_to_be_clickable(method), message)


    def get_text(self, locator):
     return self.wait_element(locator).text


    def wait_visibility(self, method, message=''):
      return self.wait.until(EC.visibility_of_element_located(method), message)  # Elementin sayfada görünür olmasını bekler

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])  # yeni açılan sekmeye geçiş yapmak için kullanılır




