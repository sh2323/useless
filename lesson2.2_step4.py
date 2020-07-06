import math
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value").text
    y = calc(int(x_element))



    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    check = browser.find_element_by_id("robotCheckbox")
    check.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    rob = browser.find_element_by_id("robotsRule")
    rob.click()


    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()