import time
from selene.support.shared import browser
from selene import be, have


class DoctorsPage:
    """Класс для тестов, связанных со страницей выбора доктора"""

    def select_doctor(self,value):
        browser.all(".b-card-nav__title").element_by(have.text("Врачи")).click()
        browser.all('[class$="b-btn_color_white"]').element_by(have.text(value)).click()
        browser.element('[class="b-toggle-block__toggle-btn"').click()
        browser.all('[class="b-text-unit__text"]').element_by(have.text("Детский хирург")).click()
        return self

    def check_selected_doctor(self):
        browser.element('[class^="h2_rating"]').should(have.text("Рейтинг"))
        return self

    def open_doctors_review(self):
        browser.element(".b-doctor-card__name-surname").click()
        browser.element('[class="b-button b-button_blue"]').click()
        return self

    def select_star(self, value):
        browser.element(f'[data-name="id_osmotr"][data-mark="{value}"]').click()
        browser.element(f'[data-name="id_efficiency"][data-mark="{value}"]').click()
        browser.element(f'[data-name="id_friendliness"][data-mark="{value}"]').click()
        browser.element(f'[data-name="id_informativity"][data-mark="{value}"]').click()
        browser.element(f'[data-name="id_recommend"][data-mark="{value}"]').click()
        return self

    def select_your_clinic(self):
        browser.all('.b-select__trigger-main-text').element_by(have.text("Выберите клинику")).click()
        browser.element('[data-placeholder*="клиника"]').click()
        return self

    def select_month(self, value):
        browser.all('.b-select__trigger-main-text').element_by(have.text("Месяц")).click()
        time.sleep(2)
        browser.all('[class="b-select__option-main-text"]').element_by(have.text(value)).click()
        return self

    def select_year(self, value):
        browser.all('.b-select__trigger-main-text').element_by(have.text("Год")).click()
        browser.all('[class="b-select__option-main-text"]').element_by(have.text(value)).click()
        return self

    def fill_feedback(self, random_like,random_dislike,random_history):
        browser.element('[name="comment"]').send_keys(random_like)
        browser.element('[name="comment_plus"]').send_keys(random_dislike)
        browser.element('[name="comment_minus"]').send_keys(random_history)
        return self

    def select_illness(self):
        browser.element('[id="s2id_autogen2"]').send_keys("ми")
        browser.all('[id*="select2-result-label-"]').element_by(have.text("Гипертрофия миндалин")).click()
        return self

    def fill_phone(self, value):
        browser.element('[type="tel"]').send_keys(value)
        browser.element('[class*="confirm b-button"]').click()
        return self

    def check_right_select(self):
        browser.element('[class*="b-phone-confirm__call-phone"]').should(
            have.text("Для подтверждения позвоните нам с этого телефона на номер"))
        return self

