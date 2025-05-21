import unittest
from utils import config, driver_factory, logger
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.profile_page import ProfilePage

class NaukriTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_factory.get_driver()
        cls.logger = logger.get_logger()

    def test_login_and_profile_check(self):
        self.logger.info("Starting test: Login and Profile Flow")

        login = LoginPage(self.driver)
        login.login(config.USERNAME, config.PASSWORD)

        home = HomePage(self.driver)
        self.assertTrue(home.is_dashboard_loaded(), "Dashboard not loaded.")

        home.go_to_profile()

        profile = ProfilePage(self.driver)
        self.assertTrue(profile.is_profile_loaded(), "Profile page not loaded.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()