"Добавление комментария"
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver=webdriver.Chrome(executable_path ='C:/chromedriver')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(1)
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(1)
ruby = driver.find_element_by_xpath("//a [@data-product_id='163']").click()
time.sleep(1)
reviews = driver.find_element_by_class_name("reviews_tab").click()
driver.execute_script("window.scrollBy(0, 600);")
stars = driver.find_element_by_class_name("star-5").click()
driver.execute_script("window.scrollBy(0, 300);")
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("George")
email = driver.find_element_by_id("email")
email.send_keys("gogen1998@mail.ru")
time.sleep(1)
submit = driver.find_element_by_id("submit").click()