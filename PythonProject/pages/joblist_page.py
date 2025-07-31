import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class JobListPage(BasePage):
    LOCATION_DROPDOWN = (By.ID, 'filter-by-location')  # location seçimi dropdown'ı
    DEPARTMENT_DROPDOWN = (By.ID, 'filter-by-department')  # department seçimi dropdown'ı
    JOBS_LIST = (By.ID, 'career-position-list')  # iş ilanlarının listelendiği container
    JOBS = (By.CLASS_NAME, 'position-list-item')  # her bir iş ilanı öğesi
    ILAN = (By.CSS_SELECTOR, '.position-list-item:nth-of-type(2)')
    VIEW_BUTTON = (By.LINK_TEXT, 'View Role') # iş ilanlarda bulunan view role butonu
    POSITION_TITLE = (By.CLASS_NAME, "position-title") # iş ilanlarında bulunan position title'ı temsil eden element
    POSITION_DEPARTMENT = (By.CLASS_NAME, 'position-department') # iş ilanlarında bulunan departman bilgisini temsil eden element
    POSITION_LOCATION = (By.CLASS_NAME, 'position-location') # iş ilanlarında bulunan lokasyon bilgisini temsil eden element
    DEPARTMENT_OPTION = (By.CSS_SELECTOR, '.job-team') # Departman opsiyonlarını temsil eden element

    def select_location(self, location_text):
        # wait ile dropdown'ın gözükmesini bekler ve işlem yapar
        location_element = self.wait_visibility(self.LOCATION_DROPDOWN)
        Select(location_element).select_by_visible_text(location_text)
        self.wait_visibility(self.JOBS)
        time.sleep(5)



    def get_selected_department(self):
        # Dropdownda QA departmanının seçili olmasına kadar bekler
        department_element = self.wait_visibility(self.DEPARTMENT_DROPDOWN)   # departman dropdown'ın görünmesini bekler
        self.wait_visibility(self.DEPARTMENT_OPTION) # dropdowndaki seçeneklerin gözükebilir olmasını bekler
        return Select(department_element).first_selected_option.text  # seçili olan option'u geri döndürür.



    def is_job_list_visible(self):
        # Lokasyon seçildikten sonra iş ilanlarının gözüküp gözükmediğini gösterir
        job_list = self.find(*self.JOBS_LIST)
        self.wait_element(self.JOBS_LIST)
        return job_list.is_displayed()

    def get_all_jobs(self):
        # İş ilanı elementlerini döndürür
        self.wait_visibility(self.JOBS)
        return self.find_all(*self.JOBS)


    def get_job_details(self, job_qa):
        # iş ilanlarında başlık, pozisyon ve lokasyonun QA ve İstanbulla ilgili olmasına bakar.
        title = job_qa.find_element(*self.POSITION_TITLE).text
        department = job_qa.find_element(*self.POSITION_DEPARTMENT).text
        location = job_qa.find_element(*self.POSITION_LOCATION).text
        return {
            "title": title,
            "department": department,
            "location": location
        }


    def hover_job_button(self):
        # View role yaazılı butona tıklayabilmesi için iş ilanının üzerine hoverlar.
        self.hover_element(*self.ILAN)
        self.wait.until(EC.presence_of_element_located(self.VIEW_BUTTON))

    def click_view_button(self):
        # View role butonuna tıklar ve ilgili sayfanın açılıp açılmadığına bakar.
        self.wait_element(self.VIEW_BUTTON)
        self.click_element(*self.VIEW_BUTTON)
        self.switch_to_new_tab()
        self.wait.until(EC.url_contains("jobs.lever.co"))
