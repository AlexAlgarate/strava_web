from __future__ import annotations

from typing import Any

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from strava_web.utils import exc_log
from strava_web.utils.config import seconds


class WebElementHandler:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver

    def open_url(self, url: str) -> None:
        self.driver.get(url)

    def find_element(
        self,
        condition: EC,
        locator: By,
        selector: str,
        element_to_wait_for: Any = None,
    ) -> WebElement:
        try:
            if element_to_wait_for:
                element: WebElement = WebDriverWait(
                    driver=element_to_wait_for, timeout=seconds
                ).until(condition((locator, selector)))
            else:
                element: WebElement = WebDriverWait(
                    driver=self.driver, timeout=seconds
                ).until(condition((locator, selector)))
            return element

        except NoSuchElementException as e:
            exc_log.exception(e)
            return None

    def fill_field(self, element: WebElement, value: str) -> None:
        if element:
            element.send_keys(value)

    def click_button(self, element: WebElement) -> None:
        if element:
            element.click()
