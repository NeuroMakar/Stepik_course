from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "#answer")
    button.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    button.click()

    button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    button.click()

    button = browser.find_element(By.XPATH, "//*[text() = 'Submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
