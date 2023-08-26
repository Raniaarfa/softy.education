from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint
import os
import json

driver = webdriver.Chrome()
url = "https://www.mytek.tn/promo-back-to-school.html"

driver.get(url)

title_element =driver.find_elements(By.CLASS_NAME, "product-item-link")
products = []

for title_element in title_element:
    title = title_element.text
    link = title_element.get_attribute("href")
    product= {
        "title": title,
        "link": link
    }
    products.append(product)

#save to json files 
working_directory = os.getcwd()
web_scraping_folder = os.path.join(working_directory,"web_scraping")
products_folder = os.path.join(web_scraping_folder,"mytek")

if not os.path.exists(products_folder):
    os.mkdir(products_folder)
for product in products:
    title = product['title'].replace("/", "").replace(" ", "")
    product_json_file = f"{title}.json"
    path = os.path.join(
        products_folder,
        product_json_file
    )
    with open(path, 'w') as json_file:
        product_string = json.dumps(product)
        json_file.write(product_string)
sleep(10)
driver.close()