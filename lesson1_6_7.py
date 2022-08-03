# python lesson1_6_7.py   Для запуска из терминала
# Ответ: 21.229701944868363


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, ".first_block input")
    for element in elements:
        element.send_keys("Мой ответ")

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

# не забываем оставить пустую строку в конце файла