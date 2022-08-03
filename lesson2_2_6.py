# python lesson2_2_6.py   Для запуска из терминала
# Ответ: 28.92869029152585
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    y = calc(browser.find_element(By.CSS_SELECTOR, "#input_value").text)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    # browser.find_element(By.ID, 'answer').send_keys(y)
    # browser.find_element(By.CSS_SELECTOR, '.form-control[required]').send_keys(y)
    """Находим текстовое поле и вводим значение 'Y'"""

    button = browser.find_element(By.TAG_NAME, "button")
    # Находим кнопку 'Submit'
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # Скролим экран до появления кнопки 'Submit'
    browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    """Находим checkbox 'I m the robot' и ставим галочку"""

    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    """Выбираем radiobutton 'Robots rule!' и активируем"""


    button.click()

    alert = browser.switch_to.alert  # переключиться на окно с alert
    alert_text = alert.text.split()  # получить строку из alert и разделяем по пробелам
    print("\033[3m\033[34m {}".format("Скопируйте это число и вставьте в окно ответа модуля:"))
    print("\033[1m\033[32m {}".format(alert_text[-1]))   # печатаем последний элемент

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()