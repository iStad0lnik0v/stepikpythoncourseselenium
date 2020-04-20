from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log
from math import sin
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button100 = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book = browser.find_element_by_id("book").click()
    browser.execute_script("window.scrollBy(0, 30);")
    xelement = browser.find_element_by_id("input_value")
    x = int(xelement.text)
    print(x)
    answer = str(log(abs(12*sin(x))))
    
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(answer)
    button = browser.find_element_by_css_selector("body > form > div > div > button").click()

    new_window = browser.window_handles[2]
    browser.get(link2)
    stepikInput = browser.find_element_by_css_selector("ember303").send_keys()
    stepikInput = browser.find_element_by_css_selector("#ember112 > div > section > div > div.attempt__inner > div.attempt__actions > button.submit-submission").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
