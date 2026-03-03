from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.common.keys import Keys


class SincHourPage(BasePage):

    CONFIG_BUTTON = (By.ID, "conf")
    DATA_BUTTON = (By.ID, "btnDate")
    IMPORT_HOUR_BUTTON = (By.CSS_SELECTOR, "button.btn.blue")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button.btn.green")
    SUCCESS_MESSAGE = (By.ID, "btnUpgradeFaceBiometrics")

    def click_settings_button(self):
        self.click(self.CONFIG_BUTTON)

    def select_brasilia_timezone(self):
        self.click(self.DATA_BUTTON)
        self.click(self.IMPORT_HOUR_BUTTON)

    def click_save_button(self):
        self.click(self.SAVE_BUTTON)
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "button.close").send_keys(Keys.ESCAPE)
        self.driver.find_element(By.CSS_SELECTOR, "button.close").send_keys(Keys.ESCAPE)

    def is_loaded(self):
        return self.waits.until_visible(self.SUCCESS_MESSAGE)
