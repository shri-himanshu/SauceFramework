import time

from selenium.webdriver.common.by import By
from utils.element_handler import ElementHandler
from utils.logger import setup_logger

logger = setup_logger(__name__)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.element_handler = ElementHandler(driver)

    def open_url(self, url):
        logger.info(f"Opening URL : {url}")
        self.driver.get(url)

    def hamburger_menu_open(self):
        self.element_handler.element_event(By.ID, 'react-burger-menu-btn', "click")
        logger.info(f"Opening Hamburger Menu ")

    def hamburger_menu_close(self):
        self.element_handler.element_event(By.ID, 'react-burger-cross-btn', "click")
        logger.info(f"Closing Hamburger Menu ")

    def cancel(self):
        self.element_handler.element_event(By.ID, "cancel", "click")

    def logout(self):
        self.hamburger_menu_open()
        time.sleep(2)
        self.element_handler.element_event(By.ID, "logout_sidebar_link", "click")
        logger.info(f"Logged Out of the SauceDemo site.")

    def take_screenshot(self, filename):
        return self.element_handler.take_screenshot(filename)
