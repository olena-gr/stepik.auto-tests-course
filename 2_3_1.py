from selenium import webdriver
import time
import math

def calc(x):
   return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_class_name("btn-primary")
button.click()

alert = browser.switch_to.alert
alert.accept()

valuex = browser.find_element_by_id("input_value")
x = int(valuex.text)

input = browser.find_element_by_id("answer")
input.send_keys(calc(x))

submit = browser.find_element_by_class_name("btn-primary")
submit.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()