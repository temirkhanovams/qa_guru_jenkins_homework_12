import pytest

from data import users
from pages.registration_page import RegistrationPage


def test_student_registration_form(test_user=users.admin):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill(test_user)
    registration_page.submit()
    registration_page.should_registered_user_with(test_user)


def test_pass1():
    pass


def test_pass2():
    pass

def test_pass3():
    pass


def test_pass4():
    pass


def test_pass5():
    pass


def test_pass6():
    pass


def test_pass7():
    pass


def test_pass8():
    pass

def test_pass9():
    pass

def test_fail10():
    assert False

def test_fail11():
    assert False

def test_fail12():
    assert False

def test_fail13():
    assert False

def test_fail14():
    assert False

def test_fail15():
    assert False

@pytest.mark.skip
def test_skipped16():
    pass

@pytest.mark.skip
def test_skipped17():
    pass

@pytest.mark.skip
def test_skipped18():
    pass

@pytest.mark.skip
def test_skipped19():
    pass

@pytest.mark.skip
def test_skipped20():
    pass



