from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(sum):
  return str(x+y)

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_id("num1")
x = int(num1.text)
num2 = browser.find_element_by_id("num2")
y = int(num2.text)

result = calc(sum)
print("sum: ", result)

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(result)

submit = browser.find_element_by_class_name("btn-default")
submit.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()