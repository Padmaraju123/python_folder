import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):

        self.driver = driver
        self.username_input = (By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']")
        self.password = (By.CSS_SELECTOR,"input[placeholder='Enter your password']")
        self.pass_show = (By.XPATH, "//small[@class='fs13']")
        self.login_button = (By.XPATH,"//button[@class='btn-primary loginButton']")



    def login(self):

        self.driver.get("https://www.naukri.com/")
        self.driver.maximize_window()

        self.driver.find_element(By.XPATH, "//a[@title='Jobseeker Login']").click()
        time.sleep(5)

        self.driver.find_element(*self.username_input).send_keys("padmaraju084@gmail.com")
        time.sleep(3)

        self.driver.find_element(*self.password).send_keys("Shiridi_Sai123@@")
        time.sleep(2)

        # self.driver.find_element(*self.pass_show).click()
        # time.sleep(3)

        self.driver.find_element(*self.login_button).click()
        time.sleep(5)



