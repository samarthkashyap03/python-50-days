from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import os,time,json
from dotenv import load_dotenv
load_dotenv()
USER_NAME=os.getenv('ACCOUNT_EMAIL')
PASSWORD=os.getenv('ACCOUNT_PASSWORD')
#Create a directory to save profile information
user_profile=os.path.join(os.getcwd(),'user_profile')
os.makedirs(user_profile,exist_ok=True)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_profile}")

driver=webdriver.Chrome(options=chrome_options)
driver.get('https://appbrewery.github.io/gym/')

#Click login button
login=driver.find_element(By.CSS_SELECTOR,'div.Navigation_rightSection__L2XbA button')
driver.implicitly_wait(1)
login.click()

if USER_NAME=="" or PASSWORD=="":
    print("Please set your email and password in the .env file.")
    #Clicks on register button
    register=driver.find_element(By.CSS_SELECTOR,'div.Login_toggleContainer__8LQrF button')
    register.click()
else:
    #Fill email and password in login fields
    email=driver.find_element(By.CSS_SELECTOR,'div.Login_formGroup__jFLXd input#email-input')
    email.click()
    email.send_keys(USER_NAME)
    driver.implicitly_wait(1)
    try:
        password_box=driver.find_element(By.CSS_SELECTOR,'div.Login_formGroup__jFLXd input#password-input')
    except NoSuchElementException:
        print('Layout has been changed')
    else:
        password_box.click()
        password_box.send_keys(PASSWORD)
        driver.implicitly_wait(1)
    #Log-in
    submit=driver.find_element(By.CSS_SELECTOR,'form#login-form button#submit-button')
    submit.click()
    driver.implicitly_wait(1)

    card=driver.find_elements(By.CSS_SELECTOR,'div[id^="day-group-tue-"]')
    print(card)


   
         
