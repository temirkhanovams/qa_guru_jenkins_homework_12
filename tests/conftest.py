from selene import browser
import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser_init():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1024
    browser.config.window_height = 780
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    yield

    browser.quit()