import time

from selenium.webdriver.common.by import By


class FinalPage:

    def __init__(self,driver):
        self.driver = driver
        self.work__options = (By.XPATH, "//div[@data-filter-id='wfhType']/div/label/p/span[1]")
        self.department_view_more_option = (By.CSS_SELECTOR,"a[id = 'functionAreaIdGid']")
        self.department_search_name = (By.XPATH,"//input[@placeholder='Search Department']")


    def work_options(self):
        work_options = self.driver.find_elements(*self.work__options)
        for option in work_options:
            if option == "Work from office":
                option.click()
                break

    def department_options(self):
        self.driver.find_element(*self.department_view_more_option).click()
        self.driver.find_element(*self.department_search_name).send_keys("engineer")

        for i in range(8,12):
            tx = self.driver.find_element(By.XPATH,"(//div[@class='styles_chckBoxCont__t_dRs']/label/p)[{0}]".format(i))
            actual_text = tx.text.split("(")[0].strip()
            if actual_text == "Engineering - Hardware & Networks":
                self.driver.find_element(By.XPATH, "(//div[@class='styles_chckBoxCont__t_dRs']/label)[{0}]".format(i)).click()

        self.driver.find_element(By.XPATH,"//div[@class='styles_filter-apply-btn__MDAUd ']").click()
        time.sleep(4)

    def package_options(self):
        self.driver.find_element(By.XPATH,"//a[@id='ctcFilter']").click()

        for v in range(12,22):
            pack = self.driver.find_element(By.XPATH,"(//div/label/p/span[@class='styles_ellipsis__cvWP1 styles_filterLabel__jRP04'])[{0}]".format(v))
            act_pack_text = pack.text.split("(")[0]
            if act_pack_text == "25-50 Lakhs":
                self.driver.find_element(By.XPATH, "(//div[@class='styles_chckBoxCont__t_dRs']/label)[{0}]".format(v)).click()

        self.driver.find_element(By.XPATH, "//div[@class='styles_filter-apply-btn__MDAUd ']").click()
        time.sleep(5)


    def selecting_company(self):
        self.driver.find_element(By.XPATH,"(//div[@class='srp-jobtuple-wrapper'])[1]").click()


    def company_description(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

        scroll_height = self.driver.execute_script("return document.body.scrollHeight")

        # Scroll step by step
        for i in range(0, scroll_height, 5):  # scroll 100px at a time
            self.driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(0.1)


    time.sleep(5)










