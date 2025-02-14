import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver_path = r"C:\Users\Raja\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)

username = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
username.click()
username.send_keys("Admin")
time.sleep(1)
password = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
password.click()
password.send_keys("admin123")
time.sleep(1)
login = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
login.click()
time.sleep(3)
pim = driver.find_element(By.LINK_TEXT, "PIM")
pim.click()
time.sleep(1)
search =driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
search.click()
search.send_keys("Raja")
time.sleep(1)
searchc=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
searchc.click()
time.sleep(1)
#Delete PIM id
deletec=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]')
deletec.click()

driver.quit()