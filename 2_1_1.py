from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector(".form-group .nowrap:nth-child(2)")
x = x_element.text
y = calc(x)

input = browser.find_element_by_id("answer")
input.send_keys(y)

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

radio = browser.find_element_by_xpath("//label[text()='Robots rule']")
radio.click()

submit = browser.find_element_by_class_name("btn-default")
submit.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()