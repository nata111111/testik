from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:/Users/1/Downloads/chromedriver_win32 (2)/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/button[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input").send_keys('Ivan')
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input").send_keys('Ivanov')
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input").send_keys('6')
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/button").click()
time.sleep(4)