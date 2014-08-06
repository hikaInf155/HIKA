import urllib.request
import csv
import os 
import re

national_debt = "http://api.worldbank.org/v2/en/indicator/gc.dod.totl.gd.zs?downloadformat=excel"
co2 = "http://api.worldbank.org/v2/en/indicator/en.atm.co2e.pc?downloadformat=excel"
agriculture_value_added = "http://api.worldbank.org/v2/en/indicator/nv.agr.totl.zs?downloadformat=excel"
tuberculosis = "http://api.worldbank.org/v2/en/indicator/sh.tbs.incd?downloadformat=excel"
GDP = "http://api.worldbank.org/v2/en/indicator/ny.gdp.mktp.cd?downloadformat=excel"


os.chdir("C://Users//HaleyPC//Documents//HIKA//Haley")
url = "http://api.worldbank.org/v2/en/indicator/ny.gdp.mktp.cd?downloadformat=excel"

def get_data(url):
	data_name = re.findall('/indicator/[a-z][a-z]\.[a-z][a-z][a-z]',url)[0][-3:]

	testfile = urllib.request.URLopener()
	testfile.retrieve(url, data_name + "_data.xls")

	import pandas as pd
	xls = pd.ExcelFile(data_name + '_data.xls')
	df = xls.parse(index_col=None, na_values=['NA'])
	df.to_csv(data_name + '_data.csv')
	return(data_name + '_data.csv')


x = get_data(agriculture_value_added)
print(x)