import math
from selenium import webdriver
import time

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    button = browser.find_element_by_class_name('trollface.btn')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id('input_value').text
    value = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(value)

    button = browser.find_element_by_class_name('btn.btn-primary')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()