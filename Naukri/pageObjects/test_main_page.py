
import time
import sys
import os

from pageObjects.final import FinalPage
from pageObjects.home import HomePage
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pageObjects.login import LoginPage


def test_e2e(browserInstance):

    driver = browserInstance


    driver.get("https://www.naukri.com/")
    driver.maximize_window()

    driver.implicitly_wait(5)

    # login page create from the file login.py
    login_page =LoginPage(driver)
    login_page.login()


    # 2nd page Home page
    home_page = HomePage(driver)
    home_page.searching_jobs()

    #3rd page final page
    final_page = FinalPage(driver)
    final_page.work_options()
    final_page.department_options()
    final_page.package_options()
    final_page.selecting_company()
    final_page.company_description()

    time.sleep(10)
    driver.close()

