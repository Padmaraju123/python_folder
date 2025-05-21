import time

from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"D:\Downloads\Webdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = Chrome(service=service_obj)

# page1
driver.get("https://www.naukri.com")
driver.maximize_window()

#login button
driver.find_element(By.XPATH,"(//div[@class='nI-gNb-header__wrapper']/div/a)[1]").click()
time.sleep(1)

#Entering the username
driver.find_element(By.XPATH,"(//div/form/div)[2]/input").send_keys("padmaraju084@gmail.com")

#Entering the password
driver.find_element(By.XPATH,"((//form)[1]/div)[3]/input").send_keys("Shiridi_Sai123@@")

#clicking the show button
# driver.find_element(By.XPATH,"(//form/div)[3]/span/small").click()
time.sleep(1)

#hidding the showed password
# driver.find_element(By.XPATH,"(//form/div)[3]/span/small").click()

#login button
driver.find_element(By.XPATH,"(//div/button)[1]").click()

time.sleep(5)


#page2
driver.find_element(By.XPATH,"//div[@class='nI-gNb-header__wrapper']/a").click()
time.sleep(2)

# scrolling the page up and down

#     scroll_height = driver.execute_script("return document.body.scrollHeight")
#
#     for i in range(0, scroll_height,10):
#         driver.execute_script(f"window.scrollTo(0, {i});")
#         time.sleep(0.1)
#
#
#     for i in range(scroll_height,0,-10):
#         driver.execute_script(f"window.scrollTo(0, {i});")
#         time.sleep(0.1)


#clicking the profile button to the right top cornor
    # driver.find_element(By.XPATH,"//div[@class='nI-gNb-bar2']").click()
    # time.sleep(4)
    #
    # driver.find_element(By.XPATH,"//a[@class='close']").click()

#clicking the search button
driver.find_element(By.XPATH,"//div[@class='nI-gNb-sb__main']/button").click()

#entering the designation
driver.find_element(By.XPATH,"(//input[@class='suggestor-input '])[1]").send_keys("Cloud")
time.sleep(2)

List_designations=driver.find_elements(By.XPATH,"//ul[@class='layer-wrap']/li")

for each_designation in List_designations:
    name = each_designation.find_element(By.XPATH,"div").text
    if name == "Cloud Engineer":
        each_designation.click()
        break


# Entering the experience in years

driver.find_element(By.XPATH,"//span[@class='ni-gnb-icn ni-gnb-icn-expand-more']").click()
list_years = driver.find_elements(By.XPATH,"//ul[@class='dropdown ']/li/div")

for each_year in list_years:
    year = each_year.find_element(By.XPATH,"span").text
    if year == "4 years":
        each_year.click()
        break

#entering the location
driver.find_element(By.XPATH,"//input[@placeholder='Enter location']").send_keys("ba")
time.sleep(2)
locations = driver.find_elements(By.XPATH,"//ul[@class='layer-wrap']/li/div")
for location in locations:
    if location.text == "Bangalore":
        location.click()
        break

driver.find_element(By.XPATH,"//span[@class='ni-gnb-icn ni-gnb-icn-search']").click()
time.sleep(5)

#page3
# work options
options = driver.find_elements(By.XPATH,"((//div[@data-type='checkbox'])[1]/div)[2]/div")

work_list = []
for op in options:
    text = op.find_element(By.XPATH,"label/p").text.split("\n")[0]
    if text == "Hybrid":
        op.click()

time.sleep(3)
#Department options
driver.find_element(By.ID,"functionAreaIdGid").click()

time.sleep(5)
driver.close()