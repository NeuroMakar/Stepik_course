from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    alert = browser.switch_to.alert.accept()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    button = browser.find_element(By.ID, "answer")
    button.send_keys(y)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    print(browser.switch_to.alert.text.split(': ')[-1])
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)

    # закрываем браузер после всех манипуляций
    browser.quit()
