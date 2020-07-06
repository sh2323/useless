import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome()
    
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '100')
        )
    
    button = browser.find_element_by_id("book")
    button.click()

    x = browser.find_element_by_id('input_value').text
    value = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(value)

    button1 = browser.find_element_by_id('solve')
    button1.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()