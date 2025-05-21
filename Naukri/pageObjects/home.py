import time
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver = driver

        self.click_search_button = (By.XPATH, "//div[@class='nI-gNb-sb__main']")

        self.designation = (By.CSS_SELECTOR,"input[placeholder='Enter keyword / designation / companies']")
        self.designations_list = (By.XPATH, "//b[@class='pre-wrap']")

        self.experience = (By.XPATH, "//span[@class='ni-gnb-icn ni-gnb-icn-expand-more']")
        self.list_exp = (By.XPATH, "//li[@class=' ']/div/span")

        self.location = (By.CSS_SELECTOR, "input[placeholder='Enter location']")
        self.list_locations = (By.XPATH, "//b[@class='pre-wrap']")

        self.search2 = (By.XPATH, "//span[@class='ni-gnb-icn ni-gnb-icn-search']")

    def searching_jobs(self):

        self.driver.find_element(*self.click_search_button).click()
        self.driver.find_element(*self.designation).send_keys("cloud engineer")
        time.sleep(5)

        Designations = self.driver.find_elements(*self.designations_list)
        for each_dig in Designations:
            if each_dig.text == "Cloud Engineer":
                each_dig.click()
                break
        time.sleep(5)

        self.driver.find_element(*self.experience).click()
        lists_exp = self.driver.find_elements(*self.list_exp)
        for ex in lists_exp:
            txt = ex.text
            if txt == "2 years":
                ex.click()
                break

        #adding the job location

        self.driver.find_element(*self.location).send_keys("bangalore")
        list_places = self.driver.find_elements(*self.list_locations)
        for place in list_places:
            tt = place.text
            if tt == "Bangalore":
                place.click()
                break

        self.driver.find_element(*self.search2).click()








