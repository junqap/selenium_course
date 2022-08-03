"""ПЕРЕХОД НА НОВУЮ ВКЛАДКУ БРАУЗЕРА"""

# При работе с веб-приложениями приходится переходить по ссылкам, которые открываются в новой вкладке браузера.
# WebDriver может работать только с одной вкладкой браузера.
# При открытии новой вкладки WebDriver продолжит работать со старой вкладкой.
# Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти.
# Это делается с помощью команды switch_to.window:

'''browser.switch_to.window(window_name)'''

# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок.
# Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:

'''new_window = browser.window_handles[1]'''

# Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:

'''first_window = browser.window_handles[0]'''

# После переключения на новую вкладку поиск и взаимодействие с элементами будут происходить уже на новой странице.

"""ЗАДАНИЕ"""
# Открыть страницу http://suninjuly.github.io/redirect_accept.html.
# Нажать на кнопку.
# Переключиться на новую вкладку.
# Пройти капчу для робота и получить число-ответ/

# python lesson2_3_6.py   Для запуска из терминала
# Ответ: 28.973057735070302

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()
    # Находим летающую кнопку и нажимаем.

    new_window = browser.window_handles[1]      # Находим имя новой вкладки
    browser.switch_to.window(new_window)        # Переходим на новую вкладку

    y = calc(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    # Получаем значение 'X' и находим по формуле 'Y'
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    # Находим поле и подставляем 'Y'

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    # Находим кнопку 'Submit' и нажимаем.

    alert = browser.switch_to.alert      # переключиться на окно с alert
    alert_text = alert.text.split()[-1]  # получить строку из alert, разделяем по пробелам и берем последний элемент
    print("\033[3m\033[34m {}".format("Скопируйте это число и вставьте в окно ответа модуля:"))     # Курсив, синий.
    print("\033[1m\033[32m {}".format(alert_text))  # Печатаем число из модального окна 'alert'.  Жирный зелёный

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()