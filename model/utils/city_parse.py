from selene.support.shared import browser
from model import app
import time


def get_cities_list():
    """Функция для получения списка городов"""
    app.given_opened()
    browser.driver.maximize_window()
    browser.element(".b-text-unit.b-text-unit_vertical_middle").click()
    time.sleep(2)
    cities = browser.all(".b-choose-town-popup__all-towns-item").locate()
    texts = [i.text for i in cities]
    return texts

