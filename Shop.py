"Отображение страницы товара"
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
shop = driver.find_element_by_xpath("// a [@href='https://practice.automationtesting.in/shop/']").click()
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(1)
book = driver.find_element_by_xpath("// a [@data-product_id='181']").click()
zagolovok = driver.find_element_by_css_selector(".product_title.entry-title").text
if zagolovok == "HTML5 Forms":
    print("Книга называется HTML5 Forms")
else:
    print("Книга называется не HTML5 Forms")


"Количество товаров в категории"
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
shop = driver.find_element_by_xpath("// a [@href='https://practice.automationtesting.in/shop/']").click()
time.sleep(1)
html = driver.find_element_by_xpath("// a [@href='https://practice.automationtesting.in/product-category/html/']").click()
time.sleep(1)
count = driver.find_elements(By.CLASS_NAME, "woocommerce-LoopProduct-link")
if len(count) == 3:
    print("На странице 3 элемента HTML")
else:
    print("На странице не 3 элемента HTML")


"Сортировка товаров"
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
shop = driver.find_element_by_xpath("// a [@href='https://practice.automationtesting.in/shop/']").click()
time.sleep(1)
driver.execute_script("window.scrollBy(0, 300);")
order = driver.find_element_by_xpath("// option [@value='menu_order']")
default = order.get_attribute("selected")
if default is not None:
    print("Выбрана сортировка по умолчанию")
else:
    print("Выбрана сортировка не по умолчанию")
from selenium.webdriver.support.select import Select
sort = driver.find_element_by_class_name("orderby")
select = Select(sort)
select.select_by_value("price-desc")
orderby = driver.find_element_by_xpath("// option [@value='price-desc']")
default1 = orderby.get_attribute("selected")
if default1 is not None:
    print("Выбрана сортировка по цене от большей к меньшей")
else:
    print("Выбрана сортировка не по цене от большей к меньшей")


"Отображение, скидка товара"
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
shop = driver.find_element_by_xpath("// a [@href='https://practice.automationtesting.in/shop/']").click()
time.sleep(1)
book = driver.find_element_by_xpath("// a [@data-product_id='169']").click()
price = driver.find_element_by_css_selector(".price > del > .woocommerce-Price-amount.amount")
price_text = price.text
assert price_text == "₹600.00"
newprice = driver.find_element_by_css_selector(".price > ins > .woocommerce-Price-amount.amount")
newprice_text = newprice.text
assert newprice_text == "₹450.00"
image = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".attachment-shop_single.size-shop_single.wp-post-image"))).click()
"В браузере всегда сразу открывается маленькое окно предпросмотра. Когда открываю эту же страницу через PYTHON, то всегда сразу картинка на весь экран"
close = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()

"Проверка цены в корзине"
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver=webdriver.Chrome(executable_path ='C:/chromedriver')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(1)
shop = driver.find_element_by_xpath("// a [@href='https://practice.automationtesting.in/shop/']").click()
time.sleep(1)
book = driver.find_element_by_xpath("// a [@data-product_id='182']").click()
time.sleep(3)
count = driver.find_element_by_class_name("cartcontents")
count_text = count.text
assert count_text == "1 Item"
amount = driver.find_element_by_class_name("amount")
amount_text = amount.text
assert amount_text == "₹180.00"
time.sleep(2)
basket = driver.find_element_by_class_name("cartcontents").click()
subtotal = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal span.woocommerce-Price-amount.amount"), "₹180.00"))
total = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total span.woocommerce-Price-amount.amount"), "₹183.60"))


"Работа в корзине"
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver=webdriver.Chrome(executable_path ='C:/chromedriver')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(1)
shop = driver.find_element_by_xpath("// a [@href='https://practice.automationtesting.in/shop/']").click()
time.sleep(1)
driver.execute_script("window.scrollBy(0, 300);")
book1 = driver.find_element_by_xpath("// a [@data-product_id='182']").click()
time.sleep(1)
book2 = driver.find_element_by_xpath("// a [@data-product_id='180']").click()
time.sleep(1)
basket = driver.find_element_by_class_name("cartcontents").click()
time.sleep(1)
# delete = driver.find_element_by_xpath("// a [@data-product_id='182']").click()
# time.sleep(3)
# undo = driver.find_element_by_xpath("// a [@href='https://practice.automationtesting.in/basket/?undo_item=4c5bde74a8f110656874902f07378009&amp;_wpnonce=530a31f9dd']").click()
"Не хочет находить и нажимать Undo"
field = driver.find_element_by_xpath("// input [@name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']").clear()
field2 = driver.find_element_by_xpath("// input [@name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
field2.send_keys("3")
update = driver.find_element_by_xpath("// input [@value='Update Basket']").click()
field3 = driver.find_element_by_xpath("// input [@name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
field3_value = field3.get_attribute("value")
assert field3_value == "3"
"Почему-то не получается вытащить текст из этого поля. Даже print ничего в консоль не выводит"
time.sleep(2)
button = driver.find_element_by_xpath("// input [@name='apply_coupon']").click()
time.sleep(1)
message = driver.find_element_by_class_name("woocommerce-error").text
print(message)


"Покупка товара"
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver=webdriver.Chrome(executable_path ='C:/chromedriver')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(1)
shop = driver.find_element_by_xpath("// a [@href='https://practice.automationtesting.in/shop/']").click()
time.sleep(1)
driver.execute_script("window.scrollBy(0, 300);")
book1 = driver.find_element_by_xpath("// a [@data-product_id='182']").click()
time.sleep(1)
basket = driver.find_element_by_class_name("cartcontents").click()
proceed = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward"))).click()
fields = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
name = driver.find_element_by_id("billing_first_name")
name.send_keys("George")
lastname = driver.find_element_by_id("billing_last_name")
lastname.send_keys("Rotblat")
email = driver.find_element_by_id("billing_email")
email.send_keys("gogen1998@mail.ru")
number = driver.find_element_by_id("billing_phone")
number.send_keys("89111654606")
country = driver.find_element_by_id("s2id_billing_country").click()
country_check = driver.find_element_by_xpath("// input [@aria-owns='select2-results-1']")
country_check.send_keys("Russia")
country_check1 = driver.find_element_by_class_name("select2-match").click()
adress = driver.find_element_by_id("billing_address_1")
adress.send_keys("Nevskiy prospect")
city = driver.find_element_by_id("billing_city")
city.send_keys("Saint-Petersburg")
state = driver.find_element_by_id("billing_state")
state.send_keys("Russia")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("123456")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
payments = driver.find_element_by_id("payment_method_cheque").click()
order = driver.find_element_by_id("place_order").click()
thanks =  WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
method = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot > tr:nth-child(3) > td"), "Check Payments"))