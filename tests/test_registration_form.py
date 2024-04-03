import allure
from allure_commons.types import Severity

from data import users
from pages.registration_page import RegistrationPage


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'TemirkhanovaMS')
@allure.feature('Запуск тестов через Selenoid')
@allure.story('story')
@allure.description('Запуск тестов registration_page на DEMOQA через Selenoid')
def test_student_registration_form(test_user=users.admin):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill(test_user)
    registration_page.submit()
    registration_page.should_registered_user_with(test_user)
