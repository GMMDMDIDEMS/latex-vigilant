import json
import logging
from typing import Union
from contextlib import contextmanager
from dataclasses import dataclass, field
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as GeckoService
from selenium.webdriver.chrome.service import Service as ChromeService

@contextmanager
def manage_driver(driver):
    try:
        yield driver
    finally:
        driver.quit()


@dataclass
class Webdriver:
    """
    A class for managing web drivers based on configuration settings.

    Attributes:
        browser (str): The name of the browser.
        headless (bool): A flag indicating whether to run the browser in headless mode.
        base_url (str): The base URL for the web driver.
        timeout (int): The timeout value in seconds.
        ad_blocking (bool): A flag indicating whether to enable ad blocking.

    Methods:
        from_config(cls, config_file): Creates a WebdriverManager instance based on the configuration file.
        initialize_browser(self): Initializes and returns a web driver instance based on the configuration settings.
    """

    browser: str
    headless: bool
    base_url: str
    timeout: int
    ad_blocking: bool
    driver: Union[webdriver.Chrome, webdriver.Firefox] = field(init=False)
    logger: logging.Logger = field(init=False)

    def __post_init__(self):
        self.logger = logging.getLogger(__name__)
        self.initialize_browser()

    def initialize_browser(self):
        if self.browser == "brave":
            options = ChromeOptions()
            options.add_argument("start-maximized")
            if self.headless is True:
                options.add_argument("--headless")
            self.driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager(
                    chrome_type=ChromeType.BRAVE).install(), options=options))
        elif self.browser == "chrome":
            options = ChromeOptions()
            options.add_argument("start-maximized")
            if self.headless is True:
                options.add_argument("--headless")
            self.driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()), options=options)
        elif self.browser == "firefox":
            options = FirefoxOptions()
            options.add_argument("start-maximized")
            if self.headless is True:
                options.add_argument("--headless")
            self.driver = webdriver.Firefox(
                service=GeckoService(GeckoDriverManager().install()), options=options)
        else:
            raise ValueError(f"Unsupported browser: '{self.browser}'")


    @classmethod
    def from_config(cls, config_file: str):
        with open(config_file, 'r', encoding='utf8') as f:
            config_data = json.load(f)

        return cls(**config_data)