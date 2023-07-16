import logging
from utils.webdriver import manage_driver, Webdriver

def main():
    logging.basicConfig(level=logging.INFO)

    CONFIG_PATH = "config.json"
    webdriver = Webdriver.from_config(CONFIG_PATH)

    with manage_driver(webdriver.driver) as driver:
        driver.get(webdriver.base_url)
        webdriver.logger.info("Opened the base URL.")


if __name__ == "__main__":
    main()