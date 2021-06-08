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


def search(query, sheet):
    driver.get("https://images.google.com")
    searchBar = driver.find_element_by_name("q")
    i=0
    searchBar.send_keys(query)
    searchBar.send_keys(Keys.RETURN)
    while(i < 20):
        showMore = driver.find_element_by_class_name("mye4qd")
        endDiv = driver.find_element_by_class_name("Yu2Dnd")
        if showMore.is_displayed() and showMore.is_enabled():
            showMore.click()
        if endDiv.is_displayed():
            break
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 100000)")
        i = i + 1

    images = driver.find_elements_by_class_name("rg_i")
    print(len(images))
    images_url = []
    count = 0

    for image in images:
        try:
            image.click()
        except:
            continue

        time.sleep(2)
        element = driver.find_elements_by_class_name('v4dQwb')

        # Google image web site logic
        if count == 0:
            try:
                big_img = element[0].find_element_by_class_name('n3VNCb')
            except:
                continue
        else:
            try:
                big_img = element[1].find_element_by_class_name('n3VNCb')
            except:
                continue

        src =  big_img.get_attribute("src")

        if(src[:4] == "data"):
            time.sleep(2)
            src = big_img.get_attribute("src")

        if(src[:4] == "data"):
            continue
        
        images_url.append(big_img.get_attribute("src"))
        sheet.write(count, 0, src)
        # write image to file
        # reponse = requests.get(images_url[count-1])
        # if reponse.status_code == 200:
        #     with open(f"wildfire/{query[:3]}{count+1}.jpg","wb") as file:
        #         file.write(reponse.content)

        count += 1


#write(sheet1)
# search("wildfires", sheet1)
# search("forest fires", sheet1)
# search("burning forests", sheet3)
# search("flames in forest", sheet1)
# search("brush fire", sheet1)
# search("bushfire", sheet6)
# search("national park fire", sheet7)




# search("water pollution", sheet1)
# search("polluted water", sheet1)
# search("industrial water pollution", sheet1)


# search("air pollution", sheet1)
search("smoke pollution", sheet1)

#CHANGE NAME OF EXCEL FILE

wb.save("air smoke pollution.xls")