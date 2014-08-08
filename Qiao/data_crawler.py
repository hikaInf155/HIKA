import urllib.request
from bs4 import BeautifulSoup
import re
page=urllib.request.urlopen('http://wdi.worldbank.org/table/3.1')
soup=BeautifulSoup(page)
for tr in soup.find_all('tr')[5:]:
    tds = tr.find_all('td')
    for i in tds:
        print(i.text,end=" ")
    print()
