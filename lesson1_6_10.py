# python lesson1_6_10.py   Для запуска из терминала
# Ответ:


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://suninjuly.github.io/registration1.html"   # Первый адрес тест проходит
# url = "http://suninjuly.github.io/registration2.html" # Второй адрес тест падает с ошибкой NoSuchElementException


# Ваш код, который заполняет обязательные поля
try:
    browser = webdriver.Chrome()
    browser.get(url)

    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first').send_keys("my first name")
    # browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
    """Находим поле 'first name' и записываем в него 'my first name'"""

    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second').send_keys("my last name")
    # browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
    """Находим поле 'last name' и записываем в него 'my last name"""

    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third').send_keys("my email")
    # browser.find_element(By.XPATH, "//input[@class='form-control third' and @required]")
    """Находим поле 'email' и записываем в него 'my email"""

    browser.find_element(By.CSS_SELECTOR, '.second_block .form-control.first').send_keys("my phone")
    """Находим поле 'phone' и записываем в него 'my phone"""

    browser.find_element(By.CSS_SELECTOR, '.second_block .form-control.second').send_keys("my city")
    """Находим поле 'address' и записываем в него 'my city"""


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

