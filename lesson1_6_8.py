# python lesson1_6_8.py   Запускает из терминала
# Ответ: 25.27275426129509


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "firstname")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')    # //button[text()="Submit"]
    button.click()

    alert = browser.switch_to.alert  # переключиться на окно с alert
    alert_text = alert.text.split()  # получить строку из alert и разделяем по пробелам
    print(f'Скопируйте это число и вставьте в окно ответа модуля: \n{alert_text[-1]}')  # печатаем последний элемент


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла