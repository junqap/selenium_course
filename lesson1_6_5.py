# python lesson1_6_5.py   Запускает из терминала
# Ответ: 25.218686063749374


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


url = "http://suninjuly.github.io/find_link_text"
amount = str(math.ceil(math.pow(math.pi, math.e)*10000))    # 224592 эта строка зашифрована в задании


try:
    browser = webdriver.Chrome()
    browser.get(url)
    link = browser.find_element(By.LINK_TEXT, amount)
    link.click()

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "firstname")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    alert = browser.switch_to.alert  # переключиться на окно с alert
    alert_text = alert.text.split()  # получить строку из alert и разделяем по пробелам
    print(f'Скопируйте это число и вставьте в окно ответа модуля: \n{alert_text[-1]}')  # печатаем последний элемент

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

