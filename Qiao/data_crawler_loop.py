import urllib.request
#Using BeautifulSoup Module
from bs4 import BeautifulSoup
import re
#Loop the websites within same indicator
for k in range(7):
    page=urllib.request.urlopen('http://data.worldbank.org/indicator/AG.LND.IRIG.AG.ZS?page='+str(k))
    soup=BeautifulSoup(page)
#Show all the data pulled from website
    for tr in soup.find_all('tr')[1:]:
        tds = tr.find_all('td')
        for i in tds:
            print(i.text,end=" ")
        print()
