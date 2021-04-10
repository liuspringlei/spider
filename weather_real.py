from pandas.core import frame
import requests
from bs4 import BeautifulSoup
import pandas as pd
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

url = 'http://www.tianqihoubao.com/yubao/handan.html' #t天气城市是邯郸
r = requests.get(url, headers=headers)
r_soup = BeautifulSoup(r.text, "lxml")
table = r_soup.find('table')
#提出日期
item = table.find_all('td', rowspan="2", align="center")
date = list()
for item in item:
    date.append(item.text)
new_date = list()
for i in date:
    new_date.append(
        i.replace("\r\n                                            ", ""))
#print(new_date)
#提出最高温度
item1 = table.find_all('td', style="color:#E54600", align="center")
high_temp = list()
for item1 in item1:
    high_temp.append(item1.text)
#print(high_temp)

#提出最低温度
item2 = table.find_all('td', style="color:#000065", align="center")
low_temp = list()
for item2 in item2:
    low_temp.append(item2.text)
#print(low_temp)

#提出天气状况
item3 = table.find_all('td', align="left")
weather = list()
for i in range(0, len(item3), 2):
    weather.append(item3[i].text)
new_weather = list()
for i in weather:
    new_weather.append(i.replace("\n\xa0\xa0\xa0", ""))
#print(new_weather)

#提出风力等级
item4 = table.find_all('td', align="center")
wind = list()
for i in range(7, len(item4), 7):
    wind.append(item4[i].text)
#print(wind)

z = list(zip(new_date, low_temp, high_temp, new_weather, wind))
frame = pd.DataFrame(z,
                     columns=['date', 'low_tp', 'high_tp', 'weather', 'wind'])
frame.to_csv('weather.csv', index=False)