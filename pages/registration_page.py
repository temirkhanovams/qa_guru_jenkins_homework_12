from data.users import User
from qa_guru_selene_homework_10 import resource
from selene import browser, be, by, command, have


class RegistrationPage:
    def __init__(self):
        self.first_name_selector = browser.element('#firstName')
        self.last_name_selector = browser.element('#lastName')
        self.email_selector = browser.element('#userEmail')
        self.gender_selector = browser.all('[name=gender]')
        self.phone_selector = browser.element('#userNumber')
        self.year_selector = browser.element('.react-datepicker__year-select')
        self.month_selector = browser.element('.react-datepicker__month-select')
        self.day_selector = browser.element('.react-datepicker__month')
        self.subjects_selector = browser.element('#subjectsInput')
        self.image_selector = browser.element('#uploadPicture')
        self.address_selector = browser.element('#currentAddress')
        self.state_selector = browser.element('#state')
        self.city_selector = browser.element('#city')
        self.state_city_value_selector = browser.all('[id^=react-select][id*=option]')
        self.submit_selector = browser.element('#submit')
        self.result_selector = browser.element('.table').all('tr td:nth-child(2)')

    def open(self):
        return browser.open(f'/automation-practice-form')

    def fill_full_name(self, first_name, last_name):
        self.first_name_selector.should(be.blank).type(first_name)
        self.last_name_selector.should(be.blank).type(last_name)

    def fill_email(self, value):
        self.email_selector.should(be.blank).type(value)

    def fill_gender(self, value):
        self.gender_selector.element_by(have.value(value)).element('..').click()

    def fill_phone(self, value):
        self.phone_selector.should(be.blank).type(value)

    def fill_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        self.year_selector.click()
        browser.element(by.text(year)).click()
        self.month_selector.click()
        browser.element(by.text(month)).click()
        self.day_selector.click()
        browser.element(by.text(day)).click()

    def fill_subjects(self, value):
        self.subjects_selector.should(be.blank).type(value).press_enter()

    def fill_hobbies(self, param):
        browser.element('#hobbies-checkbox-2').perform(command.js.scroll_into_view)
        browser.all('.custom-checkbox').element_by(have.exact_text(param)).click()

    def fill_image(self, value):
        self.image_selector.send_keys(resource.path(value))

    def fill_address(self, value):
        self.address_selector.click().type(value)

    def fill_state(self, state, city):
        self.state_selector.click()
        self.state_city_value_selector.element_by(have.exact_text(state)).click()
        self.city_selector.click()
        self.state_city_value_selector.element_by(have.exact_text(city)).click()

    def submit(self):
        self.submit_selector.perform(command.js.click)

    def fill(self, admin: User):
        self.fill_full_name(admin.first_name, admin.last_name)
        self.fill_email(admin.email)
        self.fill_gender(admin.gender)
        self.fill_phone(admin.phone)
        self.fill_birthday(admin.year, admin.month, admin.day)
        self.fill_subjects(admin.subjects)
        self.fill_hobbies(admin.hobbies)
        self.fill_image(admin.file)
        self.fill_address(admin.address)
        self.fill_state(admin.state, admin.city)

    def should_registered_user_with(self, admin: User):
        self.result_selector.should(
            have.texts(f'{admin.first_name} {admin.last_name}', {admin.email}, {admin.gender}, {admin.phone},
                {admin.birthday}, {admin.subjects}, {admin.hobbies}, {admin.file}, {admin.address},
                f'{admin.state} {admin.city}'))
