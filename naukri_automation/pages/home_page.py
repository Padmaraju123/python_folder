from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def is_dashboard_loaded(self):
        return "Dashboard" in self.driver.page_source

    def go_to_profile(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'View & Update Profile')]").click()