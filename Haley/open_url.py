import urllib.request
import csv
import xlrd



import os 
import pandas

os.chdir("C://Users//HaleyPC//Documents//HIKA//Haley")
url = "http://api.worldbank.org/v2/en/indicator/ny.gdp.mktp.cd?downloadformat=excel"

def get_data(url):

	testfile = urllib.request.URLopener()
	testfile.retrieve(url, "test_file.xls")

	import pandas as pd
	xls = pd.ExcelFile('test_file.xls')
	df = xls.parse(index_col=None, na_values=['NA'])
	df.to_csv('test_file.csv')