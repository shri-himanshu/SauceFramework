from .base_page import BasePage
from utils.element_handler import ElementHandler
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.element_handler = ElementHandler(driver)

    def enter_username(self, username):
        self.element_handler.element_event(By.ID, 'user-name', 'send_keys', username)

    def enter_password(self, password):
        self.element_handler.element_event(By.ID, 'password', 'send_keys', password)

    def click_login(self):
        self.element_handler.element_event(By.ID, 'login-button', 'click')

    def get_error_message(self, err_msg):
        return self.element_handler.element_event\
            (By.XPATH, f"//*[contains(text(), '{err_msg}')]", 'get_text')

    def login(self, url, user, password, **kwargs):
        self.open_url(url)
        self.enter_username(username=user)
        self.enter_password(password=password)
        self.click_login()