import pytest
from selene import Browser, Config
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach


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


@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {"browserName": "chrome", "browserVersion": "122.0",
                             "selenoid:options": {"enableVNC": True, "enableVideo": True}}
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub", options=options)

    browser = Browser(Config(driver))
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    # attach.add_video(browser)

    browser.quit()
