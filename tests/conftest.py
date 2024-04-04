import os

import allure
import pytest
# from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver import ChromeOptions

from utils import attach

DEFAULT_BROWSER_VERSION = "100.0"


@allure.step('Select browser version')
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser name.")
    parser.addoption('--browser_version', default='100.0',
                     help='Choose browser version. For Chrome: 99.0 or 100.0. For Firefox: 97.0 or 98.0.')


# @allure.step('Load env')
# @pytest.fixture(scope='session', autouse=True)
# def load_env():
#     load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_name = request.config.getoption('--browser_name')
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    browser_name = 'chrome'
    driver_options = ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    selenoid_capabilities = {"browserName": browser_name, "browserVersion": browser_version,
        "selenoid:options": {"enableVNC": True, "enableVideo": True}}

    driver_options.capabilities.update(selenoid_capabilities)

    # login = os.getenv('LOGIN')
    # password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        # command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=driver_options)

    browser.config.driver = driver

    yield browser
    with allure.step('Add screenshot'):
        attach.add_screenshot(browser)
    with allure.step('Add slog'):
        attach.add_logs(browser)
    with allure.step('Add HTML'):
        attach.add_html(browser)
    with allure.step('Add VIDEO'):
        attach.add_video(browser)

    browser.quit()
