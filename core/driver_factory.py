from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver():
    chrome_options = Options()
    chrome_options.add_argument(
        "--start-maximized --guest --ignore-certificate-errors --disable-popup-blocking --disable-notifications --disable-extensions"
    )

    driver = webdriver.Chrome(options=chrome_options)

    return driver
