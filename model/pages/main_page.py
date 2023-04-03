import time
from selene.support.shared import browser
from selene import be, have
from faker import Faker
import os
import random
import requests

faker = Faker('ru_RU')


class MainPage:
    """Класс для тестов, связанных с главной страницей сайта"""

    def open_main_page(self):
        browser.element(".b-intro__title.mt-0").should(have.text("Сайт отзывов о врачах №1 в России"))
        return self

    def select_city(self, value):
        browser.element(".b-text-unit.b-text-unit_vertical_middle").click()
        browser.all(".b-choose-town-popup__all-towns-item").element_by(have.text(value)).click()
        return self

    def check_selected_city(self,value):
        browser.element(".b-text-unit.b-text-unit_vertical_middle").should(have.text(value))
        return self

    def clinic_select(self,value):
        browser.all(".b-card-nav__title").element_by(have.text("Клиники")).click()
        browser.element("[alt='место']").click()
        browser.all('[class*="v-list-item__title"]').element_by(have.text(value)).click()
        browser.element('[class*="theme--light v-size--default primary"]').click()
        return self

    def check_selected_clinic(self,value):
        browser.element(f"//*[contains(text(),'{value}')]").should(be.visible)
        return self
