from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:/Users/1/Downloads/chromedriver_win32 (2)/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='login-button']").click()
driver.find_element(By.XPATH, "//*[@id='login-otp-button']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='logout-button']").click()
time.sleep(6)
