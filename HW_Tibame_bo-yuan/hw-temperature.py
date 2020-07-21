import requests
import warnings
warnings.filterwarnings("ignore")
from bs4 import BeautifulSoup
import prettytable

#From 中央氣象局 縣市溫度極值
url="https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html?ID=Tue%20Jul%2007%202020%2018:00:35%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)"

#html格式→使用BeautifulSoup來分析
r = requests.get(url)
html = BeautifulSoup(r.text)

# print(html)
# with codecs.open("weather.html","w","utf8") as file:
#     file.write(str(html))

form = prettytable.PrettyTable(["地區","氣溫"],encoding="utf8") #建立一個 PrettyTable表格
form.align["地區"]="l" #設定欄位的對其方式
form.align["氣溫"]="l" #設定欄位的對其方式

#TODO:分層尋找
for box in html.find_all(name="tr"):
    # print(box)
    city = box.find(name="th",scope="row")
    # print(city.text)
    temperatue = box.find(name="span",class_="tem-C is-active")
    # print(temperatue.text)

    form.add_row([city.text,temperatue.text]) #新增表格的一個列

print(form) #把表格顯示出來

