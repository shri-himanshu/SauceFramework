from .base_page import BasePage
from utils.element_handler import ElementHandler
from selenium.webdriver.common.by import By
from utils.logger import setup_logger

logger = setup_logger(__name__)


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.element_handler = ElementHandler(driver)

    def continue_shopping(self):
        self.element_handler.element_event(By.ID, "continue-shopping", "click")
        logger.info(f"Going back to Inventory Page")

    def checkout(self):
        self.element_handler.element_event(By.ID, "checkout", "click")
        logger.info(f"Moving to Checkout Step One !!")


class CheckoutStepOne(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.element_handler = ElementHandler(driver)

    def continue_btn(self):
        self.element_handler.element_event(By.ID, "continue", "click")
        logger.info(f"Moving to Checkout Step Two ..")

    def first_name(self, firstname):
        self.element_handler.element_event(By.ID, 'first-name', 'send_keys', firstname)

    def last_name(self, lastname):
        self.element_handler.element_event(By.ID, 'last-name', 'send_keys', lastname)

    def postal_code(self, postalcode):
        self.element_handler.element_event(By.ID, 'postal-code', 'send_keys', postalcode)

    def fill_form(self, firstname, lastname, postalcode):
        self.first_name(firstname=firstname)
        self.last_name(lastname=lastname)
        self.postal_code(postalcode=postalcode)
        logger.info(f"Filled the Checkout Step One Form with {firstname} {lastname}  and {postalcode}")


class CheckoutStepTwo(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.element_handler = ElementHandler(driver)

    def finish(self):
        self.element_handler.element_event(By.ID, "finish", "click")
        logger.info(f"Final Check out..")


class CheckoutComplete(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.element_handler = ElementHandler(driver)

    def back_to_products(self):
        self.element_handler.element_event(By.ID, "back-to-products", "click")
        logger.info(f"Taking you back to Inventory Page..")

    def checkout_complete_page(self):
        return self.element_handler.element_event(By.XPATH, "//*[contains(text(), 'Checkout: Complete!')]", 'get_text')

