from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import os,time,json

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=chrome_options)
driver.get('https://appbrewery.github.io/gym/')

#Create a directory to save profile information
user_profile=os.path.join(os.getcwd(),'user_profile')
os.makedirs(user_profile,exist_ok=True)
text_file=os.path.join(user_profile,'profile_info.txt')

#Click login button
login=driver.find_element(By.CSS_SELECTOR,'div.Navigation_rightSection__L2XbA button')
time.sleep(1)
login.click()

try:
    f=open(f"{os.getcwd()}\\user_profile\\profile_info.txt",'r')
except FileNotFoundError:
    f=open(f"{os.getcwd()}\\user_profile\\profile_info.txt",'w')
time.sleep(1)

if f.read()=="":
    print("Please register")
    #Clicks on register button
    register=driver.find_element(By.CSS_SELECTOR,'div.Login_toggleContainer__8LQrF button')
    register.click()
    #Waits for user input
    name_input=driver.find_element(By.CSS_SELECTOR,'div.Login_formGroup__jFLXd input')
    WebDriverWait(driver,10).until(lambda d:name_input.get_attribute('value'))
    name=name_input.get_attribute('value')
    time.sleep(5)
    with open(f"{os.getcwd()}\\user_profile\\profile_info.txt",'a') as f:
        json.dump({"Name":name},f)
    email_input=driver.find_element(By.CSS_SELECTOR,'div.Login_formGroup__jFLXd #email-input')
    email_input.click()
    WebDriverWait(driver,10).until(lambda d:email_input.get_attribute('value'))
    email=email_input.get_attribute('value')
    time.sleep(5)   
    with open(f"{os.getcwd()}\\user_profile\\profile_info.txt",'a') as f:
        json.update({"Email":email},f)
         
