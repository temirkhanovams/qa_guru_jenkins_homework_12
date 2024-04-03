import allure
import pytest
from allure_commons.types import Severity

from data import users
from pages.registration_page import RegistrationPage


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'TemirkhanovaMS')
@allure.feature('Запуск тестов через Selenoid')
@allure.story('story')
@allure.description('Запуск тестов registration_page на DEMOQA через Selenoid')
def test_student_registration_form(setup_browser, test_user=users.admin):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill(test_user)
    registration_page.submit()
    registration_page.should_registered_user_with(test_user)


def test_pass1():
    pass

def test_pass2():
    pass

def test_fail1():
    assert False

def test_fail2():
    assert False

@pytest.mark.skip
def test_skipped1():
    pass

@pytest.mark.skip
def test_skipped2():
    pass