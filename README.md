## :heavy_check_mark: В проекте реализованы следующие проверки:

:radio_button: Изменение геолокации путем выбора города из списка

:radio_button: Проверка авторизации путем ввода номера мобильного телефона

:radio_button: Проверка поиска доктора

:radio_button: Проверка написания отзыва о работе доктора

:radio_button: Проверка поиска клиники по округу

---
Общая настройка для запуска тестов :

В командной строке прописать :
- pip install poetry

- poetry lock

- poetry install 

Для запуска тестов локально необходимо :

1. В файле .env определить номер мобильного телефона для  сайта prodoctorov.ru
  
2. Удалить параметр autouse=true из фикстуры selenoid_config в файлe conftest.py

3. В командной строке прописать: pytest tests/tests/py

---

Для запуск тестов с помощью Selenoid необходимо:

1. В файле .env определить :
 
       1.1 Номер мобильного телефона для сайта prodoctorov.ru
  
       1.2 Логин и пароль для Selenoid
       
  
2. Прописать параметр autouse=true в фикстуру selenoid_config в файле conftest.py

3. В командной строке прописать: pytest tests/tests.py

---
 ### Запуск в Jenkins : [JOB](https://jenkins.autotests.cloud/job/pro_doctorov_andrechizh8/)
 
 Нажать на кнопку Собрать сейчас
![Альтернативный текст](https://github.com/andrechizh8/pro_doctorov/blob/main/readme_files/4doctor.png)

После сборки есть возможность посмотреть отчет с различными приложениями: 

Скриншот:

![Альтернативный текст](https://github.com/andrechizh8/pro_doctorov/blob/main/readme_files/1doctor.png)

Видео :

![Альтернативный текст](https://github.com/andrechizh8/pro_doctorov/blob/main/readme_files/2doctor.gif)

Кроме того, в проекте реализована возможность просмотр отчета в  Allure TestOps : 

![Альтернативный текст](https://github.com/andrechizh8/pro_doctorov/blob/main/readme_files/5doctor.png)

И интеграция с Jira :

![Альтернативный текст](https://github.com/andrechizh8/pro_doctorov/blob/main/readme_files/6doctor.png)

После прохождения тестов с использованием Jenkins, в телеграмм приходит оповещение с результатами :

![Альтернативный текст](https://github.com/andrechizh8/pro_doctorov/blob/main/readme_files/3doctor.png)
