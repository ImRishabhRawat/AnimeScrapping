from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium. webdriver. chrome. options import Options
import time

se=input("Enter a Topic you want to know : ")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)


driver.maximize_window()
driver.get('https://animixplay.to/')


#container=driver.find_element(By.ID,'searchbox')
search = driver.find_element(By.ID,'q')
search.send_keys(se)
time.sleep(5)
search.send_keys(Keys.ENTER)
time.sleep(8)

all_div = driver.find_element(By.XPATH,'//*[@id="result1"]/ul/li[1]')
l=all_div.find_element(By.LINK_TEXT,se)
l.click()
time.sleep(60*24)