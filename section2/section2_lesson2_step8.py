from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname").send_keys("firstname")
    input2 = browser.find_element(By.NAME, "lastname").send_keys("lastname")
    input3 = browser.find_element(By.NAME, "email").send_keys("email")

    with open('test1.txt', 'w') as file:
        file.write('test1 for mls 228')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test1.txt')  # добавляем к этому пути имя файла
    button1 = browser.find_element(By.ID, "file").send_keys(file_path)

    button2 = browser.find_element(By.XPATH, "//*[text() = 'Submit']")
    button2.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)

    os.remove('test1.txt')
    # закрываем браузер после всех манипуляций
    browser.quit()
