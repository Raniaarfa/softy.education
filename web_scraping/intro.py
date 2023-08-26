from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "https://www.tunisianet.com.tn/pc-de-bureau/63877-mini-pc-msi-cubi5-10m-009beu-i3-10e-gen.html"

driver.get(url)
product = {}

#get data
title_element = driver.find_element(By.Class_Name , "h1")
title = title_element.text
product["title"]=title

title_element = driver.find_element(By.Class_Name , "h1")
title = title_element.text
product["title"]=title


time.sleep(1)
driver.close()

