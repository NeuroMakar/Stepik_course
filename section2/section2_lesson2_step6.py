from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
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

    people_radio = browser.find_element(By.ID, "peopleRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", people_radio)
    # Либо скрыть footer:
    # footer = browser.find_element(By.CLASS_NAME, "bd-footer")
    # browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)

    # Либо скролить Python'ом:
    # from selenium.webdriver.common.keys import Keys
    # browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)  # или Home если наверх

    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    # или:
    assert people_checked == "true", "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None
    robots_radio.click()

    button = browser.find_element(By.XPATH, "//*[text() = 'Submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
