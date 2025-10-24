from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from .base_page import BasePage
import time


class QAJobsPage(BasePage):
    

    SEE_ALL_QA = (By.XPATH, "//a[contains(., 'See all QA jobs')]")
    LOCATION_DROPDOWN = (By.ID, "select2-filter-by-location-container")
    DEPARTMENT_DROPDOWN = (By.ID, "select2-filter-by-department-container")
    JOB_LIST = (By.CSS_SELECTOR, "div.position-list-item, div[data-id='job-item']")
    VIEW_ROLE = (By.XPATH, "//a[contains(., 'View Role')]")

    def open_qa_page(self):
        self.visit("https://useinsider.com/careers/quality-assurance/")
        print("QA sayfası açıldı")
        time.sleep(3)
        try:
            cookie_btn = (By.ID, "wt-cli-accept-all-btn")
            self.wait.until(EC.element_to_be_clickable(cookie_btn)).click()
            print("Cookie banner kapatıldı")
        except:
            print("Cookie banner görünmedi")

    def click_see_all(self):
        self.click(self.SEE_ALL_QA)
        print("'See all QA jobs' tıklandı")
        time.sleep(4)

    def filter_jobs(self):


       
        for step in ["1", "2", "3"]:
            print(f"{step} 'All' kutusuna tıklama")
            box = self.wait.until(EC.element_to_be_clickable(self.LOCATION_DROPDOWN))
            box.click()
            time.sleep(2)

        print("'Istanbul, Turkiye' seçiliyor...")

        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.select2-results__option")))
        options = self.driver.find_elements(By.CSS_SELECTOR, "li.select2-results__option")
        found = False

        for opt in options:
            text = opt.text.strip().lower()
            if text == "istanbul, turkiye" or text == "istanbul, türkiye":
                self.driver.execute_script("arguments[0].scrollIntoView(true);", opt)
                time.sleep(1)
                try:
                    opt.click()
                except:
                    self.driver.execute_script("arguments[0].click();", opt)
                print("'Istanbul, Turkiye' seçildi.")
                found = True
                break

        if not found:
            raise Exception("'Istanbul, Turkiye' listede bulunamadı!")

        time.sleep(2)

        print("Department açılıyor...")
        self.wait.until(EC.element_to_be_clickable(self.DEPARTMENT_DROPDOWN)).click()
        time.sleep(1)

        print("'Quality Assurance' seçiliyor...")
        qa_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//li[contains(., 'Quality Assurance')]")))
        self.driver.execute_script("arguments[0].click();", qa_option)
        print("'Quality Assurance' seçildi.")
        time.sleep(3)

    def verify_filtered_jobs(self):
        jobs = self.driver.find_elements(*self.JOB_LIST)
        assert len(jobs) > 0, "Filtre sonrası job listesi boş!"

        for job in jobs:
            t = job.text.lower()
            print(f"Job: {t.replace(chr(10), ' | ')}")
            assert "quality assurance" in t, "Job Position QA içermiyor"
            assert "istanbul" in t, "Job Location Istanbul içermiyor"

        print("Tüm joblar QA & Istanbul filtresine uyuyor.")

    def click_first_view_role(self):
        print("View Role butonları aranıyor...")

       
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        view_roles = self.driver.find_elements(By.XPATH, "//a[contains(., 'View Role')]")
        assert len(view_roles) > 0, "View Role butonu bulunamadı"

        first = view_roles[0]

        old_tabs = self.driver.window_handles

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first)
        time.sleep(1)

        try:
            first.click()
        except:
            self.driver.execute_script("arguments[0].click();", first)

        time.sleep(3)

        new_tabs = self.driver.window_handles
        assert len(new_tabs) > len(old_tabs), "View Role tıklandı ama yeni sekme açılmadı!"

        self.driver.switch_to.window(new_tabs[-1])
        time.sleep(3)

        current_url = self.driver.current_url.lower()
        print(f"Yeni sekme URL: {current_url}")

        assert "lever.co" in current_url, "Lever sayfasına yönlendirilmedi!"
        print("Başarıyla Lever başvuru sayfasına yönlendirildi")
