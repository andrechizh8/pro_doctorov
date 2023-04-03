import pytest
from model import app
import allure
from allure_commons.types import Severity
from model.data.user import current_user


class TestUi:

    @pytest.mark.main_page
    @allure.tag('UI', 'WEB')
    @allure.description('med_rocket UI test')
    @allure.label('owner', 'andrechizh8')
    @allure.feature('UI')
    @allure.story('check right page')
    @allure.severity(Severity.CRITICAL)
    def test_check_right_page(self):
        # GIVEN
        with allure.step("Open main page"):
            app.given_opened()

        # WHEN
        with allure.step("Check right page"):
            app.main_page.open_main_page()

    @pytest.mark.city
    @allure.tag('UI', 'WEB')
    @allure.description('med_rocket UI test')
    @allure.label('owner', 'andrechizh8')
    @allure.feature('UI')
    @allure.story('check change geo')
    @allure.severity(Severity.CRITICAL)
    def test_select_city(self):
        # GIVEN
        with allure.step("Open main page"):
            app.given_opened()

        # WHEN
        with allure.step("Select city"):
            app.main_page.select_city(current_user.city)

        # THEN
        with allure.step("Check selected city"):
            app.main_page.check_selected_city(current_user.city)

    @pytest.mark.auth
    @allure.tag('UI', 'WEB')
    @allure.description('med_rocket UI test')
    @allure.label('owner', 'andrechizh8')
    @allure.feature('UI')
    @allure.story('check auth')
    def test_phone_auth(self):
        # GIVEN
        with allure.step("Open main page"):
            app.given_opened()

        # WHEN
        with allure.step("Open auth page"):
            app.auth_page.login_window()

        with allure.step("Check selected auth"):
            app.auth_page.check_auth_selected()

        # THEN
        with allure.step("Select phone auth"):
            app.auth_page.phone_auth(current_user.phone_number)

    @pytest.mark.doctor
    @allure.tag('UI', 'WEB')
    @allure.description('med_rocket UI test')
    @allure.label('owner', 'andrechizh8')
    @allure.feature('UI')
    @allure.story('check doctors select')
    def test_select_doctor(self):
        # GIVEN
        with allure.step("Open main page and select city"):
            self.test_select_city()

        # WHEN
        with allure.step("Select doctor"):
            app.doctors_page.select_doctor(current_user.doctor_area)

        # THEN
        with allure.step("Check doctor selected"):
            app.doctors_page.check_selected_doctor()

    @pytest.mark.review
    @allure.tag('UI', 'WEB')
    @allure.description('med_rocket UI test')
    @allure.label('owner', 'andrechizh8')
    @allure.feature('UI')
    @allure.story('check doctors review')
    def test_doctors_review(self):
        # GIVEN
        with allure.step("Open main page and select city"):
            self.test_select_doctor()
        # WHEN
        with allure.step("Open doctors review page"):
            app.doctors_page.open_doctors_review()

        with allure.step("Select rating"):
            app.doctors_page.select_star(current_user.doctor_star)

        with allure.step("Select clinic"):
            app.doctors_page.select_your_clinic()

        with allure.step("Select date"):
            app.doctors_page.select_month(current_user.month)
            app.doctors_page.select_year(current_user.year)

        with allure.step("Fill feedback info"):
            app.doctors_page.fill_feedback(random_like=current_user.random_like,
                                           random_dislike=current_user.random_dislike,
                                           random_history=current_user.random_history)

        with allure.step("Fill illness info"):
            app.doctors_page.select_illness()

        with allure.step("Fill users phone"):
            app.doctors_page.fill_phone(current_user.phone_number)

        # THEN
        with allure.step("Check right filling"):
            app.doctors_page.check_right_select()

    @pytest.mark.clinic
    @allure.tag('UI', 'WEB')
    @allure.description('med_rocket UI test')
    @allure.label('owner', 'andrechizh8')
    @allure.feature('UI')
    @allure.story('check clinic select')
    def test_clinic_select(self):
        # GIVEN
        with allure.step("Open main page and select city"):
            self.test_select_city()

        # WHEN
        with allure.step("Select clinic by region"):
            app.main_page.clinic_select(current_user.user_region)

        # THEN
        with allure.step("Check selected region"):
            app.main_page.check_selected_clinic(current_user.user_region)
