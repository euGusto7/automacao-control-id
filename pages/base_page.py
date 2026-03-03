from utils.waits import Waits


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.waits = Waits(driver)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        element = self.waits.until_clickable(locator)
        element.click()

    def type(self, locator, text):
        element = self.waits.until_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.waits.until_visible(locator)
        return element.text

    def find_element(self, locator):
        return self.waits.until_visible(locator)
