class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def is_profile_loaded(self):
        return "Profile Snapshot" in self.driver.page_source