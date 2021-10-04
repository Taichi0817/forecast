#!/usr/bin/env python
# coding: utf-8

# In[24]:


import datetime
import urllib.request as req
import requests
from bs4 import BeautifulSoup
import re

url = "https://notify-api.line.me/api/notify"
access_token = 'XXX'
headers = {'Authorization': 'Bearer ' + access_token}


url2 = "https://tenki.jp/forecast/5/26/5110/23106/"   
res = requests.get(url2)                              
soup = BeautifulSoup(res.content, 'html.parser')      


ddd = soup.find(class_="left-style")                  

telop = soup.find("p", class_="weather-telop").string

highlists = soup.find("dd",class_="high-temp temp")

lowlists = soup.find("dd",class_="low-temp temp")

ttt = soup.find(class_="rain-probability")

row=[]
for t in ttt:
    row.append(t)


message="\n" + "名古屋市中区栄の天気" + "\n"+ ddd.text + "\n" + "\n" + "----------" + "\n" + telop + "\n" + "----------" + "\n" +  "\n" + "最高　" + highlists.text + "\n" + "最低　" + lowlists.text + "\n"+ "---------" + "\n" +row[1].text +"\n" + "~6  : " + row[3].text + "\n" + "~12 : " + row[5].text +"\n" + "~18 : " + row[7].text +"\n" + "~24 : " + row[9].text +"\n"

payload = {'message': message}
r = requests.post(url, headers=headers, params=payload,)


# In[26]:


get_ipython().system('jupyter nbconvert --to python forecast.ipynb')


# In[ ]:





# In[ ]:




