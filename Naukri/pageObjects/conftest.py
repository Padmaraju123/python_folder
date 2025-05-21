import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help = "browser selection")

@pytest.fixture(scope="function")
def browserInstance(request):

    browser_name = request.config.getoption("browser_name")


    if browser_name == "chrome":
        service_obj = Service(r"D:\Downloads\Webdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service = service_obj, options=chrome_options)

    elif browser_name == "firefox":
        service_obj = Service(r"D:\Downloads\Webdrivers\geckodriver-v0.34.0-win64\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)


    yield driver