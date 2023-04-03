from selene.support.shared import browser
from model.pages.main_page import MainPage
from model.pages.auth_page import AuthPage
from model.pages.doctors_page import DoctorsPage
import os
from dotenv import load_dotenv

load_dotenv()

main_page = MainPage()
auth_page = AuthPage()
doctors_page = DoctorsPage()


def given_opened():
    """Открытие главной страницы"""

    url = os.getenv("BASE_URL")
    browser.open(url)
