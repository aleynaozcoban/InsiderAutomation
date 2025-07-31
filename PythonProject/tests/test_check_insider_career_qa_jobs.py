import time
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.department_page import DepartmentPage
from pages.joblist_page import JobListPage


class TestCheckInsiderCareerQaJobs(BaseTest):

    def test_check_insider_career_qa_jobs(self):
        home_page = HomePage(self.driver)
        home_page.close_cookie_banner()
        time.sleep(5)
        self.assertEqual(self.base_url, home_page.get_current_url(), 'anasayfada değilsiniz.')
        home_page.hover_menu_company()
        home_page.click_menu_careers()

        careers_page = CareersPage(self.driver)
        self.assertTrue(careers_page.is_block_visible(), 'kariyer sekmesindeki bloklar görünmüyor')
        # Kariyer sayfasında teams, location, life at insider bloklarının görünüp görünmediğini kontrol eder

        self.driver.get("https://useinsider.com/careers/quality-assurance/")

        department_page = DepartmentPage(self.driver)
        department_page.click_job()  # See all QA jobs butonuna tıklar


        joblist_page = JobListPage(self.driver)
        self.assertIn("Quality Assurance", joblist_page.get_selected_department(), 'Quality Assurance değil')
        # iş ilanları sayfasında departman seçiminde Quality Assurance seçili mi değil mi diye bakar

        joblist_page.select_location("Istanbul, Turkiye")
        time.sleep(15)

        # iş ilanları sayfasında konum şeçiminde Istanbul, Turkiye seçimini yapar.

        self.assertTrue(joblist_page.is_job_list_visible(), "İş ilanları listesi görünmüyor")
        # İş ilanları gözüküyor mu onu kontrol eder.

        jobs = joblist_page.get_all_jobs()

        for job in jobs:
            details = joblist_page.get_job_details(job)
            title = details["title"]
            department = details["department"]
            location = details["location"]

            self.assertIn("Quality Assurance", title, f"Pozisyon adında 'Quality Assurance' yok: {title}")
            self.assertIn("Quality Assurance", department, f"Departman bilgisi yanlış: {department}")
            self.assertIn("Istanbul", location, f"Lokasyon bilgisi yanlış: {location}")
            # her bir iş ilanı için istenilen bilgilerin bulunup bulunmadığını kontrol eden for döngüsü

        joblist_page.hover_job_button()
        joblist_page.click_view_button()  # istenilen ilana başvurmak için butona tıklanmasını sağlar
        time.sleep(5)

        self.assertIn("jobs.lever.co", self.driver.current_url, "Yönlendirme Lever başvuru sayfasına yapılmadı.")
        # butona tıkladıktan sonra ilgili sayfaya yönlendirme yapıyor mu diye kontrol edergit init
