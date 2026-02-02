from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name=driver.find_element(By.CSS_SELECTOR,'.form-signin input.form-control.top')
f_name.click()
time.sleep(3)
f_name.send_keys('Samarth')
time.sleep(3)
l_name=driver.find_element(By.CSS_SELECTOR,'.form-signin input.form-control.middle')
l_name.click()
l_name.send_keys('kashyap')
time.sleep(2)
email=driver.find_element(By.CSS_SELECTOR,'.form-signin input.form-control.bottom')
email.click()
email.send_keys('samarthkashyap.12345@gmail.com')
time.sleep(2)
sign_up=driver.find_element(By.TAG_NAME,'button')
sign_up.click()
time.sleep(2)
