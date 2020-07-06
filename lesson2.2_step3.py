from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

try:
    sum = 0
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1").text
    y_element = browser.find_element_by_id("num2").text
    sum = int(x_element) + int(y_element)
    

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum))



    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()