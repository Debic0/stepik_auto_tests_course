from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import os
import math

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Firefox()
    browser.get(link)

    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_path = os.path.join(current_dir, 'file.txt')

    # input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    # input1.send_keys("Василий")

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']")
    # input2.send_keys("Пупкин")

    # input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']")
    # input3.send_keys("vasiliy.pupkin@mail.com")

    # input1 = browser.find_element(By.CSS_SELECTOR, "input#file")
    # input1.send_keys(file_path)

    #button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    #button.click()

    # confirm = browser.switch_to.alert
    # confirm.accept()
    
    #new_window = browser.window_handles[1]
    #browser.switch_to.window(new_window)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button1 = browser.find_element(By.CSS_SELECTOR, "button#book")
    button1.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(y)

    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn#solve")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)