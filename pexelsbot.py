from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import xlwt
from xlwt import Workbook

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')


def search(sheet):
    driver.get("https://www.pexels.com/search/city%20pollution/")
    i=0
    while(i < 10):
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 100000)")
        i = i + 1

    images = driver.find_elements_by_class_name("photo-item__img")
    print(len(images))
    images_url = []
    count = 0

    for image in images:
        src = image.get_attribute("srcset")
        source = src.split("?")[0]
        images_url.append(source)
        sheet.write(count, 0, source)
        count += 1


search(sheet1)
wb.save("city_air_pollution_pexels.xls")