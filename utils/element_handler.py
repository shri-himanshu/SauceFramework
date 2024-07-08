import os
import time

from utils.logger import setup_logger
from selenium.webdriver.common.action_chains import ActionChains

logger = setup_logger(__name__)


class ElementHandler:
    def __init__(self, driver):
        self.driver = driver

    def element_event(self, by, identifier, event, data=None):
        try:
            element = self.driver.find_element(by, identifier)
        except Exception as ui_err:
            logger.error(f"Raised Exception when searching element {identifier}: Traceback -> {ui_err}")
        if event == 'send_keys':
            element.send_keys(data)
        elif event == 'click':
            element.click()
        elif event == 'hover':
            ActionChains(self.driver).move_to_element(element).perform()
        elif event == 'get_text':
            return element.text
        elif event == 'get_attribute':
            return element.get_attribute(data)
        # Add more events as needed
        else:
            raise ValueError(f"Unsupported event: {event}")

    def take_screenshot(self, test_name, result):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshots_dir = os.path.join(os.getcwd(), 'reports', 'screenshots')
        os.makedirs(screenshots_dir, exist_ok=True)
        filename = f"{test_name}_{result}_{timestamp}.png"
        screenshot_path = os.path.join(screenshots_dir, filename)
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path
