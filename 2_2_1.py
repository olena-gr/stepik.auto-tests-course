from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

valuex = browser.find_element_by_id("input_value")
x = int(valuex.text)

result = calc(x)

input = browser.find_element_by_id("answer")
input.send_keys(result)

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

radio = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()

button = browser.find_element_by_class_name("btn-primary")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()