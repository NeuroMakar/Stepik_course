from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 15 секунд, пока кнопка "price" не станет "100":
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID, "book").click()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "#answer")
    button.send_keys(y)

    button = browser.find_element(By.XPATH, "//*[text() = 'Submit']")
    button.click()

finally:
    print(browser.switch_to.alert.text.split(': ')[-1])
    time.sleep(5)
    browser.quit()
