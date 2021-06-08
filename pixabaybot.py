from urllib.request import urlopen
  
# import json
import json

import xlwt
from xlwt import Workbook

# store the URL in url as 
# parameter for urlopen
url = "https://pixabay.com/api/?key=21978755-d8af7d021c8224f78d2c030b9&q=dirty+air&image_type=photo&pretty=true"

  
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
results = data_json["hits"]
count = 0

print(len(results))
print(data_json["totalHits"])

for result in results:
    small_src = result["previewURL"]
    sheet.write(count, 0, small_src)
    count += 1

# wb.save("air_pollution_pixabay.xls")
# wb.save("bad_city_air_pixabay.xls")
# wb.save("bad_air_pixabay.xls")
# wb.save("polluted_air_pixabay.xls")
wb.save("dirty_air_pixabay.xls")