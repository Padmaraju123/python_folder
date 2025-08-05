# https://automationexercise.com/
import logging
import sys
import os
import time

from openpyxl.workbook import Workbook

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
import pytest
from PageObjects.login import LoginPage
from PageObjects.Signup import SignUpPage
import pyautogui

with open(r"C:\Users\HP\Documents\Playwright_project\Data\NewUser.json", "r") as f:
    new_user_data = json.load(f)
    users = new_user_data["NewUser"]


@pytest.mark.parametrize("get_details", users)
def test_1(playwright, get_details):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000, args=["--start-maximized"])
    context_obj = browser.new_context(no_viewport=True)
    page = context_obj.new_page()

    username = get_details["username"]
    user_mail = get_details["email_id"]
    passd = get_details["password"]
    mnth = get_details["month"]
    dte = get_details["date"]
    yr = get_details["year"]
    first_name = get_details["first_name"]
    last_name = get_details["last_name"]
    company_name = get_details["company"]
    given_add = get_details["address"]
    country_name = get_details["country"]
    state_name = get_details["state"]
    city_name = get_details["City"]
    pin_code = get_details["Pincode"]
    mobile_no = get_details["Mobile No"]

    Details = [username, user_mail, passd, dte, mnth, yr, first_name,
               last_name, company_name, given_add, country_name, state_name, city_name,
               pin_code, mobile_no]

    new_obj = SignUpPage(page)
    new_obj.navigate()
    new_obj.Creating_user(Details)

    # Signup
    # page.get_by_placeholder("Name").fill("Padmaraju")
    # page.locator("[data-qa='signup-email']").fill("padmaraju084@gmail.com")
    # page.get_by_role("button", name="Signup").click()
    # page.locator("#id_gender1").click()
    # page.locator("#password").fill("AutomationPractice123@@")

    # Confirmation message after the signup


#
# def test_contact():
#     page.get_by_role("link", name="Contact us").click()
#
#     page.locator("//input[@name='name']").fill("Padmaraju")
#     page.locator("input[data-qa='email']").fill("padmaraju084@gmail.com")
#     page.get_by_placeholder("Subject").fill("Feedback about website")
#     page.locator("#message").fill("""Hi, the website is very helpful to do automation with customize way and completely user
# friendly mode.
#
#
# Thanks
# Padmaraju""")
#     page.locator("input[data-qa='submit-button']").click()
#     time.sleep(5)
#
#
# def test_logout():
#     page = self.page
#     time.sleep(5)
#     page.locator("//a[text()=' Logout']").click()
# ------------------------------------------------------------------------------------

with open(r"C:\Users\HP\Documents\Playwright_project\Data\credentials.json", "r") as f:
    data = json.load(f)
    user_data = data["user_credentials"]


@pytest.mark.parametrize("user_credential", user_data)
def test_Invalid_valid_credentials(playwright, user_credential):
    user_mail = user_credential["login_email"]
    user_pass = user_credential["password"]

    browser = playwright.chromium.launch(headless=False, slow_mo=1000, args=["--start-maximized"])
    context_obj = browser.new_context(no_viewport=True)
    page = context_obj.new_page()

    # actually browser interactions starts here
    # creating obj of the class: LoginPage in login.py from the pageObject directory

    login_obj = LoginPage(page)
    login_obj.navigate_url()
    login_obj.user_details(user_mail, user_pass)


def test_Dashboard(playwright):

    browser = playwright.chromium.launch(headless=False, slow_mo=1000, args=["--start-maximized"])

    context_obj = browser.new_context(no_viewport=True, record_video_dir=r"C:\Users\HP\Documents\Playwright_project"
                                                                         r"\Recorded_videos",
                                      record_video_size={"width": 1920, "height": 1080})

    page = context_obj.new_page()

    page.goto("https://automationexercise.com/")
    print("The url of the page is {}".format(page.url))
    page.get_by_role("link", name=" Signup / Login").click()

    page.locator("//input[@data-qa='login-email']").fill("padmaraju084@gmail.com")
    page.get_by_placeholder('Password').fill("AutomationPractice123@@")
    page.get_by_role("button", name="Login").click()

    page.evaluate("""
        (async () => {
            let distance = 100;
            while (window.scrollY + window.innerHeight < document.body.scrollHeight) {
                window.scrollBy(0, distance);
                await new Promise(resolve => setTimeout(resolve, 120));
            }
        })();
    """)

    page.evaluate("window.scrollTo({ top: 0, behavior: 'smooth' })")
    time.sleep(2)

    page.locator("//a[@href='#Men']/span").click()
    time.sleep(3)

    page.get_by_text("Tshirts").click()

    products = page.locator("//div[@class='productinfo text-center']/a")
    products_count = products.count()

    for i in range(products_count):
        products.nth(i).click()
        page.locator("//button[@class='btn btn-success close-modal btn-block']").click()
        time.sleep(2)

    page.locator("(//a[@href='/view_cart'])[1]").click()
    time.sleep(5)

    page.evaluate("""
            (async () => {
                let distance = 100;
                while (window.scrollY + window.innerHeight < document.body.scrollHeight) {
                    window.scrollBy(0, distance);
                    await new Promise(resolve => setTimeout(resolve, 200));
                }
            })();
        """)

    page.evaluate("window.scrollTo({ top: 0, behavior: 'smooth' })")
    time.sleep(5)

    Wb = Workbook()
    wb_sheet = Wb.active
    wb_sheet.title = "Cart Details"
    wb_sheet.append(["Product name", "Price", "Quantity", "Total_price"])

    names = page.locator("//td[@class='cart_description']/h4")
    cc = names.count()
    product_names = []

    quantities = page.locator("//td[@class='cart_quantity']/button")
    quantity_list = []

    prices = page.locator("//td[@class='cart_price']/p")
    price_list = []

    total_prices = page.locator("//td[@class='cart_total']/p")
    total_list = []

    for i in range(cc):
        product = names.nth(i).text_content()
        product_names.append(product)

        each_price = prices.nth(i).text_content()
        price_list.append(each_price)

        each_quantity = quantities.nth(i).text_content()
        quantity_list.append(each_quantity)

        each_total = total_prices.nth(i).text_content()
        total_list.append(each_total)

    for k in range(cc):
        wb_sheet.append([product_names[k], price_list[k], quantity_list[k], total_list[k]])

    Wb.save(r"C:\Users\HP\Documents\Playwright_project\Cart_Data\cart_details.xlsx")

    page.locator("//a[text()='Proceed To Checkout']").click()

    page.evaluate("""
                   (async () => {
                       let distance = 100;
                       while (window.scrollY + window.innerHeight < document.body.scrollHeight) {
                           window.scrollBy(0, distance);
                           await new Promise(resolve => setTimeout(resolve, 200));
                       }
                   })();
               """)

    page.evaluate("window.scrollTo({ top: 0, behavior: 'smooth' })")
    time.sleep(5)

    page.get_by_role("link", name="Place Order").click()

    time.sleep(10)

    context_obj.close()
    browser.close()
