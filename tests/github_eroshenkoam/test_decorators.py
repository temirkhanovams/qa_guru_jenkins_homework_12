import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import allure


def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("76")

@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open('https://github.com/')

@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s("#query-builder-test ").submit()

@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text("eroshenkoam/allure-example")).click()


@allure.step("Открываем tab issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text("#" + number)).should(be.visible)