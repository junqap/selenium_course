# python lesson2_1_5.py   Для запуска из терминала
# Ответ: 28.881817554078573


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    # x_element = browser.find_element(By.CSS_SELECTOR, "#input_value") # Находим х =  на странице
    # x = x_element.text    # Выделяем значение х
    # y = calc(x)   # Подставляем х в формулу
    y = calc(browser.find_element(By.CSS_SELECTOR, "#input_value").text)    # Замена трёх предыдущих строк

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    # browser.find_element(By.ID, 'answer').send_keys(y)
    # browser.find_element(By.CSS_SELECTOR, '.form-control[required]').send_keys(y)
    """Находим текстовое поле и вводим значение 'Y'"""

    browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    """Находим checkbox 'I m the robot' и ставим галочку"""

    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    """Выбираем radiobutton 'Robots rule!' и активируем"""

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    """Нажимаем на кнопку Submit"""

    alert = browser.switch_to.alert  # переключиться на окно с alert
    alert_text = alert.text.split()  # получить строку из alert и разделяем по пробелам
    print("\033[3m\033[34m {}".format("Скопируйте это число и вставьте в окно ответа модуля:"))
    print("\033[1m\033[32m {}".format(alert_text[-1]))  # печатаем последний элемент

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()