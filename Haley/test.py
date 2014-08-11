import urllib.request
import re
import csv
import json
import os

os.chdir("C://Users//HaleyPC//Documents//HIKA//Haley")

def get_data(url):
    data_name = re.findall('/indicator/[a-z][a-z]\.[a-z][a-z][a-z]\.[a-z][a-z][a-z,0-9][a-z,0-9]',url)[0][-7:]

    testfile = urllib.request.URLopener()
    testfile.retrieve(url, data_name + "_data.xls")

    import pandas as pd
    xls = pd.ExcelFile(data_name + '_data.xls')
    df = xls.parse(index_col=None, na_values=['NA'])
    df.to_csv(data_name + '_data.csv')
    return(data_name + '_data.csv')

d = get_data("http://api.worldbank.org/v2/en/indicator/sp.dyn.le00.in?downloadformat=excel")
print(d)