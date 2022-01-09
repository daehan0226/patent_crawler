import time
from random import uniform

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from src.exceptions import ElementByTypeError, ElementInfoError, WrongPageError, SwitchTabError, AlertTimeoutError, NoElementError

from config.config import config


class DriverManager:
    driver = webdriver.Chrome(config["driver"])

    def __init__(self, logging):
        self._wait = config["wait"]
        self._implicitly_wait = config["implicitly_wait"]
        self._logging = logging

    def _random_wait_sleep(self):
        time.sleep(uniform(self._wait, self._wait + 1))

    def _return_element_info_if_valid(self, element_info):
        try:
            by, target = element_info
        except ValueError:
            raise ElementInfoError(element_info)
        
        if by not in ["css", "xpath"]:
            raise ElementByTypeError(by)
        
        return by, target

    def _find_element(self, element_info):
        by, target = self._return_element_info_if_valid(element_info)
        try:
            if by == "css":
                return self.driver.find_element_by_css_selector(target)
            elif by == "xpath":
                return self.driver.find_element_by_xpath(target)
        except NoSuchElementException:
            raise NoElementError(target)

    def get(self, url):
        self._logging.info(f"loading url : {url}")
        self._random_wait_sleep()
        self.driver.get(url)
        self.driver.implicitly_wait(self._implicitly_wait)
    
    def raise_error_if_wrong_page(self, title):
        if title not in self.driver.title:
            raise WrongPageError

    def quit(self):
        self._logging.info(f"finished")
        self._random_wait_sleep()
        self.driver.quit()

    def click_button(self, element):
        self._random_wait_sleep()
        self._find_element(element).click()
        self._logging.debug(f"clicked the button {element[0]} : {element[1]}")

    def send_text_to_input(self, element, text):
        self._random_wait_sleep()
        self._find_element(element).clear()
        self._find_element(element).send_keys(text)
        self._logging.debug(f"sent text to input {element[0]} : {element[1]}")

    def switch_tab(self, index):
        self._random_wait_sleep()
        try:
            self.driver.switch_to.window(self.driver.window_handles[index])        
            self._logging.debug(f"switched tab to {index}")
        except IndexError:
            raise SwitchTabError(index)

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
            raise AlertTimeoutError(wait)

    def click_checkbox_label(self, parent, target, check_all_element_text=None):
        """
        check_all_element can check or uncheck all including target input checkbox
        do not check/uncheck check_all_element if check_all_element is provided
        """
        self._random_wait_sleep()
        parent_element = self._find_element(parent)
        label_elements = parent_element.find_elements_by_css_selector("label")
        for label_element in label_elements:
            if check_all_element_text is not None and label_element.text in check_all_element_text:
                continue

            input_id = label_element.get_attribute("for")
            input_element = parent_element.find_element_by_id(input_id)
            if label_element.text in target:
                if 'false' == input_element.get_attribute("checked"):
                    input_element.click()
            else:
                if 'true' == input_element.get_attribute("checked"):
                    input_element.click()

    def select_sort(self, parent, target, order_element):
        self._random_wait_sleep()
        self.click_button(parent) # show select options
        parent_element = self._find_element(parent)
        option_elements = parent_element.find_elements_by_css_selector("button")

        for option_element in option_elements:
            if option_element.text == target:
                option_element.click()
                break
        self.click_button(order_element)
        