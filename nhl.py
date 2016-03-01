# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 14:25:52 2016

@author: jaredl
"""

from bs4 import BeautifulSoup
import requests
r = requests.get('http://www.nhl.com/scores/htmlreports/20152016/PL020902.HTM')
data = r.text
soup = BeautifulSoup(data)
print type(soup)

table_code = soup.find_all('tr', class_="evenColor")

rowid = []
for i in range(len(table_code)):
    temp = table_code[i].find('td', class_ = 'bborder')
    temp = temp.get_text()
    rowid.append(temp)