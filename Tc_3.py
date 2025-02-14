import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver_path = r"C:\Users\Raja\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.maximize_window()
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
time.sleep(2)

pim = driver.find_element(By.LINK_TEXT, "PIM")
pim.click()
time.sleep(1)
add = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")
add.click()
time.sleep(1)
#Create a PIM account
firstname = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
firstname.click()
firstname.send_keys("Raja")
time.sleep(1)
lastname = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
lastname.click()
lastname.send_keys("Gowthaman")
time.sleep(3)
save = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
save.click()
# driver.quit()