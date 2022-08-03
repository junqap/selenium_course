# python lesson2_4_8.py   Для запуска из терминала
# Ответ: 29.016342696931247

"""ЗАДАНИЕ"""
# Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене.
# Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), '100'))

    browser.find_element(By.CSS_SELECTOR, "#book").click()
    # Находим кнопку 'Book' и нажимаем.

    y = calc(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    # Получаем значение 'X' и находим по формуле 'Y'
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    # Находим поле и подставляем 'Y'

    browser.find_element(By.CSS_SELECTOR, "#solve").click()
    # Находим кнопку 'Submit' и нажимаем.


    alert = browser.switch_to.alert      # переключиться на окно с alert
    alert_text = alert.text.split()[-1]  # получить строку из alert, разделяем по пробелам и берем последний элемент
    print("\033[3m\033[34m {}".format("Скопируйте это число и вставьте в окно ответа модуля:"))     # Курсив, синий.
    print("\033[1m\033[32m {}".format(alert_text))  # Печатаем число из модального окна 'alert'.  Жирный зелёный

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

