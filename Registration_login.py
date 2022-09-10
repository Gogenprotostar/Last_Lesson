"Регистрация аккаунта"
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver=webdriver.Chrome(executable_path ='C:/chromedriver')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(1)
account = driver.find_element_by_id("menu-item-50").click()
mail = driver.find_element_by_id("reg_email")
mail.send_keys("gogen1998@mail.ru")
password = driver.find_element_by_id("reg_password")
password.send_keys("Protostar123!")
time.sleep(2)
user = driver.find_element_by_id("username")
user.send_keys("123")
"Без убирания курсора из поля ввода пароля для регистрации, кнопка REGISTER не кликается"
register = driver.find_element_by_xpath("// input [@name='register']").click()


"Логин в систему"
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver=webdriver.Chrome(executable_path ='C:/chromedriver')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(1)
account = driver.find_element_by_id("menu-item-50").click()
user = driver.find_element_by_id("username")
user.send_keys("gogen1998@mail.ru")
passw = driver.find_element_by_id("password")
passw.send_keys("Protostar123!")
register = driver.find_element_by_xpath("// input [@name='login']").click()
logout = driver.find_element_by_xpath("// a [@href='https://practice.automationtesting.in/my-account/customer-logout/']")
if logout is not None:
    print("Элемент есть")
else:
    print("Элемента нет")