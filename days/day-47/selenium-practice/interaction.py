from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
time.sleep(3)
number_of_articles=driver.find_elements(By.XPATH,"//a[@title='Special:Statistics']")
print(number_of_articles[1].text)