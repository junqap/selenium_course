from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import math


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    first_name = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
    first_name.send_keys('Test')    # /html/body/div/form/div[1]/div[1]/input
    last_name = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
    last_name.send_keys('Test')
    email_field = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
    email_field.send_keys('qwer@QWER.COM')
    phone_field = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input")
    phone_field.send_keys("12345678")
    address_field = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input")
    address_field.send_keys('UA')
    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




