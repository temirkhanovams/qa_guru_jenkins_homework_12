import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import allure
from allure_commons.types import Severity


def test_no_labels():
    pass


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('issue в репозитории')
    allure.dynamic.story('Неавторизованный пользователь может создать issue в репозитории')
    allure.dynamic.link('http://github.com', name='Testing')
    pass


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'TemirkhanovaMS')
@allure.feature('issue в репозитории')
@allure.story('Авторизованный пользователь может создать issue в репозитории')
@allure.link('http://github.com', name='Testing')
def test_decorator_labels():
    pass
