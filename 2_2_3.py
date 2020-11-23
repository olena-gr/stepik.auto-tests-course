from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector("[name = 'firstname']")
input1.send_keys("wer")

input2 = browser.find_element_by_css_selector("[name = 'lastname']")
input2.send_keys("eds")

input3 = browser.find_element_by_css_selector("[name = 'email']")
input3.send_keys("sdsd")

sendFile = browser.find_element_by_id("file")
current_dir = os.path.abspath(os.path.dirname('2_2_3.py'))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, '2_1.txt')           # добавляем к этому пути имя файла 
sendFile.send_keys(file_path)

submit = browser.find_element_by_class_name("btn-primary")
submit.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()