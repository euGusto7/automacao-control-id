from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (By.ID, "input_user")
    PASSWORD = (By.ID, "input_password")
    LOGIN_BUTTON = (By.ID, "logar")
    TIMELINE = (By.ID, "timeline_200199")

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def is_timeline_loaded(self):
        return self.waits.until_visible(self.TIMELINE)
