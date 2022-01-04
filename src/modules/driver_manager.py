import time
from random import uniform

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from src.modules.logger import Logger
from config.config import config


class DriverManager:
    driver = webdriver.Chrome(config["driver"])

    def __init__(self, wait=1):
        self._wait = wait
        self._logging = Logger("crawler")

    def _random_wait_sleep(self):
        time.sleep(uniform(self._wait, self._wait + 1))

    def _find_element(self, elemnet_info):
        by, target = elemnet_info
        if by == "css":
            return self.driver.find_element_by_css_selector(target)
        elif by == "xpath":
            return self.driver.find_element_by_xpath(target)

    def get(self, url):
        self._random_wait_sleep()
        self._logging.info(f"loading url : {url}")
        try:
            self.driver.get(url)
        except Exception as e:
            self._logging.error(f"loading url error, {e.__str__()}")

    def quit(self):
        self._random_wait_sleep()
        self._logging.info(f"finished")
        self.driver.quit()

    def click_button(self, element):
        self._random_wait_sleep()
        self._logging.debug(f"click button by {element[0]} : {element[1]}")
        try:
            self._find_element(element).click()
        except Exception as e:
            self._logging.error(f"click button error, {e.__str__()}")

    def send_text_to_input(self, element, text):
        self._random_wait_sleep()
        self._logging.debug(f"send text to input by {element[0]} : {element[1]}")
        try:
            self._find_element(element).clear()
            self._find_element(element).send_keys(text)
        except Exception as e:
            self._logging.error(f"send text to input error, {e.__str__()}")

    def switch_tab(self, index):
        self._random_wait_sleep()
        self.driver.switch_to.window(self.driver.window_handles[index])

    def select_options(self, source, target, move_btn):
        source_element = self._find_element(source)
        options = source_element.find_elements_by_xpath("./*")
        for option in options:
            if option.text in target:
                option.click()
                self._find_element(move_btn).click()

    def get_text(self, element):
        self._random_wait_sleep()
        text = self._find_element(element).text
        self._logging.debug(f"parse text : {text}")
        return text

    def wait_for_alert(self, wait):
        try:
            WebDriverWait(self.driver, wait).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()

        except TimeoutException:
            self._logging.error(f"wait for alert error")

    def click_checkbox_label(self, parent, target, check_all_element_text=None):
        """
        check_all_element can check or uncheck all including target input checkbox
        do not check/uncheck check_all_element if check_all_element is provided
        """
        source_element = self._find_element(parent)
        label_elements = source_element.find_elements_by_css_selector("label")
        for label_element in label_elements:
            if check_all_element_text is not None and label_element.text in check_all_element_text:
                continue

            input_id = label_element.get_attribute("for")
            input_element = source_element.find_element_by_id(input_id)
            if label_element.text in target:
                if 'false' == input_element.get_attribute("checked"):
                    input_element.click()
            else:
                if 'true' == input_element.get_attribute("checked"):
                    input_element.click()