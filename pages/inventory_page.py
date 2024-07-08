from .base_page import BasePage
from utils.element_handler import ElementHandler
from selenium.webdriver.common.by import By
from utils.logger import setup_logger

logger = setup_logger(__name__)

# mapping of Add/Remove to cart buttons xpath ids
inventory_items = {
    "backpack": ("add-to-cart-sauce-labs-backpack", "remove-sauce-labs-backpack"),
    "bikelight": ("add-to-cart-sauce-labs-bike-light", "remove-sauce-labs-bike-light"),
    "tshirt": ("add-to-cart-sauce-labs-bolt-t-shirt", "remove-sauce-labs-bolt-t-shirt"),
    "fleece": ("add-to-cart-sauce-labs-fleece-jacket", "remove-sauce-labs-fleece-jacket"),
    "onesie": ("add-to-cart-sauce-labs-onesie", "remove-sauce-labs-onesie"),
    "redtshirt": ("add-to-cart-test.allthethings()-t-shirt-(red)", "remove-test.allthethings()-t-shirt-(red)")
}

# mapping of item links to view full page
item_links = {
    "bikelight": ("item_0_title_link", "item_0_img_link"),
    "tshirt": ("item_1_title_link", "item_1_img_link"),
    "onesie": ("item_2_title_link", "item_2_img_link"),
    "redtshirt": ("item_3_title_link", "item_3_img_link"),
    "backpack": ("item_4_title_link", "item_4_img_link"),
    "fleece": ("item_5_title_link", "item_5_img_link")
}

# mapping of Dropdown selections
dropdown = {
    "AtoZ": "az",
    "ZtoA": "za",
    "lowtohigh": "lohi",
    "hightolow": "hilo"
}


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.element_handler = ElementHandler(driver)

    def is_at(self):
        # Implement logic to verify if you are on the inventory page
        # Example:
        return "inventory.html" in self.driver.current_url

    def add_to_cart(self, items):
        # Implement adding items to cart
        for item in items:
            self.element_handler.element_event(By.ID, inventory_items[item][0], "click")
            # to validate if the button click was success
            try:
                remove_btn = self.element_handler.element_event(By.ID, inventory_items[item][1], "get_text")
            except UnboundLocalError as add_fail_err:
                raise RuntimeError(f"Failed to add the {item} to cart with error : {add_fail_err}")

            logger.info(f"{item} added to cart successfully.")

    def remove_from_cart(self, item):
        # Implement removing items from cart
        try:
            self.element_handler.element_event(By.ID, inventory_items[item][1], "click")
        except UnboundLocalError as remove_fail_err:
            raise RuntimeError(f"Failed to remove the {item}; No such item in cart")

        logger.info(f"{item} removed from cart successfully.")

    def go_to_cart(self):
        # Method to navigate to the cart page
        self.element_handler.element_event(By.XPATH, "//a[@class='shopping_cart_link']", "click")
        logger.info(f"Going to Cart ...")

    def drop_down_filter(self, selection):
        self.element_handler.element_event(By.XPATH, '//select', 'click')
        self.element_handler.element_event(By.XPATH, f'//option[@value="{dropdown[selection]}"]', 'click')
        logger.info(f"Inventory Items successfully sorted in {dropdown[selection]} way.")

    def check_inventory_img_source(self, item):
        img_src = self.element_handler.element_event(By.XPATH,
                                                     f'//*[@id="{item_links[item][1]}"]/img', 'get_attribute', 'src')
        logger.info(f"Collected the image source for {item} from Inventory Home page..")
        return img_src

    def item_title_link(self, item):
        self.element_handler.element_event(By.ID, item_links[item][0], "click")
        logger.info(f"Jumping to Item {item} title page..")

    def item_link_img_src(self):
        logger.info(f"Collecting the image source for from Item Title page..")

        return self.element_handler.element_event(
            By.XPATH, f'//*[@id="inventory_item_container"]/div/div/div[1]/img', 'get_attribute', 'src')

    def back_to_products(self):
        self.element_handler.element_event(By.ID, "back-to-products", "click")

    # Add more methods as per your application's functionality
