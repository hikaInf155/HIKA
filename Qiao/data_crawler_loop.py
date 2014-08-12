import urllib.request
from bs4 import BeautifulSoup
import re
for k in range(7):
    page=urllib.request.urlopen('http://data.worldbank.org/indicator/AG.LND.IRIG.AG.ZS?page='+str(k))
    soup=BeautifulSoup(page)
    for tr in soup.find_all('tr')[1:]:
        tds = tr.find_all('td')
        for i in tds:
            print(i.text,end=" ")
        print()
