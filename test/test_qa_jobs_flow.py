from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage

def test_qa_jobs(driver):
    home = HomePage(driver)
    home.open_home_page()
    assert "Insider" in driver.title

  
    home.go_to_careers()
    careers = CareersPage(driver)
    careers.check_blocks()

 
    qa = QAJobsPage(driver)
    qa.open_qa_page()
    qa.click_see_all()
    qa.filter_jobs()
    qa.verify_filtered_jobs()
    qa.click_first_view_role()
