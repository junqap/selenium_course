"""Работа со списками"""
# python lesson2_2_3.py   Для запуска из терминала
# Ответ: 28.927325923495673     28.927325995808896
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def sum(x, y):
    return str(x + y)

url = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)


    num1 = int(browser.find_element(By.ID, "num1").text)                # Получить число num1
    num2 = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)     # Получить число num2
    summa = sum(num1, num2)      # Посчитать сумму заданных чисел и представить строкой

    # select = Select(browser.find_element(By.TAG_NAME, "select"))
    # select.select_by_value(summa)   # Выбрать в выпадающем списке значение равное 'summa'
    Select(browser.find_element(By.TAG_NAME, "select")).select_by_value(summa)
    """Выбрать в выпадающем списке значение равное 'summa'"""

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