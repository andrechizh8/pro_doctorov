import os
import random
from dataclasses import dataclass
from faker import Faker
from typing import Literal
from dotenv import load_dotenv


@dataclass
class User:
    phone_number: str
    city: Literal['Барнаул', 'Владивосток', 'Волгоград', 'Воронеж',
    'Екатеринбург', 'Ижевск', 'Казань', 'Краснодар', 'Красноярск', 'Нижний Новгород',
    'Новосибирск', 'Омск', 'Пермь', 'Ростов-на-Дону', 'Самара', 'Саратов', 'Тольятти', 'Ульяновск', 'Уфа', 'Челябинск', 'Ярославль']
    random_history: str
    random_like: str
    random_dislike: str
    month: str
    year: str
    star: int
    doctor_area: Literal['Взрослые', 'Детские', 'Стоматологи']
    doctor_star: int
    user_region : Literal['Западный округ','Карасунский округ','Прикубанский округ','Центральный округ']


faker = Faker('ru_RU')

current_user = User(phone_number=os.getenv("PHONE_NUMBER"), city="Краснодар",
                    month=random.choice(['Январь', 'Ферваль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август',
                                         'Сентябрь', 'Октябрь', 'Ноябрь', 'Ферваль']),
                    year="2022",
                    random_like=faker.first_name() * 40,
                    random_dislike=faker.first_name(),
                    random_history=faker.first_name(),
                    star=random.randint(-2, 3),
                    doctor_area="Детские",
                    doctor_star=random.randint(-2, 2),
                    user_region="Прикубанский округ")
