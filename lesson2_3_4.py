""" МОДАЛЬНЫЕ ОКНА - ALERT, CONFIRM, PROMPT"""
# Чтобы получить текст из alert, используйте свойство text объекта alert:
'''
alert = browser.switch_to.alert
alert_text = alert.text
'''
# Другой вариант модального окна, который предлагает пользователю выбор согласиться
# с сообщением или отказаться от него, называется confirm.
# Для переключения на окно confirm используется та же команда, что и в случае с alert:
'''
confirm = browser.switch_to.alert
confirm.accept()
'''
# Для confirm-окон можно использовать следующий метод для отказа:
'''
confirm.dismiss()
'''
# Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста.
# Чтобы ввести текст, используйте метод send_keys():
'''
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept() или confirm.dismiss()
'''

""" ЗАДАНИЕ: """

# Открыть страницу 'http://suninjuly.github.io/alert_accept.html'
# Нажать на кнопку
# Принять 'confirm'
# На новой странице решить капчу для роботов, чтобы получить число с ответом


# python lesson2_3_4.py   Для запуска из терминала
# Ответ: 28.97218915217524

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    """Находим кнопку и "КЛИКАЕМ" по ней"""

    # confirm = browser.switch_to.alert     # модальное окно confirm
    # confirm.accept()                      # принять его с помощью команды accept()
    browser.switch_to.alert.accept()        # Замена двух строк предыдущих

    y = calc(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    # Получаем значение 'X' и находим по формуле 'Y'
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    # Находим поле и подставляем значение 'Y'.

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    # Находим кнопку 'Submit' и нажимаем.

    alert = browser.switch_to.alert         # переключиться на окно с alert
    alert_text = alert.text.split()[-1]     # получить строку из alert, разделяем по пробелам и берем последний элемент
    print("\033[3m\033[34m {}".format("Скопируйте это число и вставьте в окно ответа модуля:"))
    print("\033[1m\033[32m {}".format(alert_text))  # печатаем последний элемент

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()