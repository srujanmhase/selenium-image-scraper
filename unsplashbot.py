# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import requests
# import xlwt
# from xlwt import Workbook

# path = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(path)

# # Workbook is created
# wb = Workbook()
  
# # add_sheet is used to create sheet.
# sheet1 = wb.add_sheet('Sheet 1')


# def search(sheet):
#     driver.get("https://unsplash.com/s/photos/forest-fires")
#     i=0

#     while(i < 10):
#         time.sleep(3)
#         driver.execute_script("window.scrollBy(0, 100000)")
#         i = i + 1

#     images = driver.find_elements_by_class_name("_2UpQX")
#     imagelist = driver.find_elements_by_tag_name("img")
#     print(len(imagelist))

#     images_url = []
#     count = 0

#     for image in imagelist:
#         try:
#             src = image.get_attribute("srcset")
#         except:
#             continue
#         source = src.split(" ")[0]
#         images_url.append(source)
#         sheet.write(count, 0, source)
#         count += 1


# search(sheet1)
# wb.save("forest_fires_unsplash.xls")
# import urllib library
from urllib.request import urlopen
  
# import json
import json

import xlwt
from xlwt import Workbook

# store the URL in url as 
# parameter for urlopen
url = "https://unsplash.com/napi/search?query=dirty%20air&xp=&per_page=100000"

  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())
  
# print the json response
# print(data_json)
# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet = wb.add_sheet('Sheet 1')
results = data_json["photos"]["results"]
count = 0

print(len(results))
print(data_json["photos"]["total"])

for result in results:
    small_src = result["urls"]["small"]
    sheet.write(count, 0, small_src)
    count += 1

# wb.save("air_pollution_unsplash.xls")
# wb.save("bad_city_air_unsplash.xls")
# wb.save("bad_air_unsplash.xls")
# wb.save("polluted_air_unsplash.xls")
# wb.save("air_mask_unsplash.xls")
# wb.save("dirty_air_unsplash.xls")