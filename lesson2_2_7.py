# python lesson2_2_6.py   Для запуска из терминала
# Ответ: 28.929597684438765

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    browser.find_element(By.CSS_SELECTOR, 'input[name = "firstname"]').send_keys('my first name')
    """Находим поле 'first name' и записываем в него 'my first name'"""

    browser.find_element(By.CSS_SELECTOR, 'input[name = "lastname"]').send_keys('my last name')
    """Находим поле 'last name' и записываем в него 'my last name"""

    browser.find_element(By.CSS_SELECTOR, 'input[name = "email"]').send_keys('my email')
    """Находим поле 'email' и записываем в него 'my email"""

    current_dir = os.path.abspath(os.path.dirname(__file__))
    """получаем путь к директории текущего исполняемого файла"""

    file_path = os.path.join(current_dir, 'file.txt')
    """добавляем к этому пути имя файла"""

    browser.find_element(By.ID, 'file').send_keys(file_path)
    """Находим элемент 'Выберите файл' и записываем файл на сайт"""


    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    """Нажимаем на кнопку Submit"""

    alert = browser.switch_to.alert     # переключиться на окно с alert
    alert_text = alert.text.split()     # получить строку из alert и разделяем по пробелам

    print("\033[3m\033[34m {}".format("Скопируйте это число и вставьте в окно ответа модуля:"))     # Курсив Синий
    print("\033[1m\033[32m {}".format(alert_text[-1]))      # печатаем последний элемент Жирный Зелёный
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()