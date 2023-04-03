from selene.support.shared import browser
from selene import be, have


class AuthPage:
    """Класс для тестов, связанных с авторизацией"""

    def login_window(self):
        browser.element('[class^="b-choose-login-type"]').click()
        browser.element('[href*="login"]').click()
        return self

    def check_auth_selected(self):
        browser.element('.my-0.headline').should(have.text("Личный кабинет пациента"))
        return self

    def phone_auth(self,value):
        browser.element("[inputmode='tel']").send_keys(value).press_enter()
        return self
