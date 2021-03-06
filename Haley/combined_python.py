"""This module changes our csv data into json format"""
import urllib.request
import re
import csv
import json
import os
from collections import OrderedDict

os.chdir("C://Users//HaleyPC//Documents//HIKA//Haley")

def get_data(url):
    data_name = re.findall('/indicator/[a-z][a-z]\.[a-z][a-z][a-z]\.[a-z][a-z][a-z][a-z]',url)[0][-7:]

    testfile = urllib.request.URLopener()
    testfile.retrieve(url, data_name + "_data.xls")

    import pandas as pd
    xls = pd.ExcelFile(data_name + '_data.xls')
    df = xls.parse(index_col=None, na_values=['NA'])
    df.to_csv(data_name + '_data.csv')
    return(data_name + '_data.csv')


def fix_country_names(file_name):
    
    csv_list=list()
    with open(file_name, 'rt',encoding='utf8') as csvfile:
        spamreader = csv.reader(csvfile,delimiter=',', quotechar='"')
        for row in spamreader:
            csv_list.append(row)
    countries = list()
    #print(csv_list)

    for i in range(0, len(csv_list)):
        del csv_list[i][0]

    for i in range(3,len(csv_list)):
        countries.append(csv_list[i][0])
    #make names of data easier

    if file_name == "atm.co2e_data.csv":
        csv_list[3][2] = "CO2"
    if file_name == "agr.totl_data.csv":
        csv_list[3][2] = "Agriculture"
    if file_name == "tbs.incd_data.csv":
        csv_list[3][2] = "Tuberculosis"
    if file_name == "gdp.mktp_data.csv":
        csv_list[3][2] = "GDP"
    if file_name == "dod.totl_data.csv":
        csv_list[3][2] = "National Debt"
    if file_name == "dyn.cbrt_data.csv":
        csv_list[3][2] = "Birth Rate"
    if file_name == "dyn.le00_data.csv":
        csv_list[3][2] = "Life Expectancy"
    
    #get rid of problems with countries that have commas in the name
    countries[22] = 'Bahamas, The'
    countries[47] = 'Congo, Rep.'
    countries[70] = 'Egypt, Arab Rep.'
    countries[82] = 'Micronesia, Fed. Sts'
    countries[88] = 'Gambia, The'
    countries[98] = 'Hong Kong SAR, China'
    countries[109] = 'Iran, Islamic Rep.'
    countries[123] = 'Korea, Rep.'
    countries[144] = 'Macao SAR, China'
    countries[156] = 'Macedonia, FYR'
    countries[192] = 'Korea, Dem. Rep.'
    countries[246] = 'Venezuela, RB'
    countries[253] = 'Yemen, Rep.'
    countries[255] = 'Congo, Dem. Rep.'

    #deleting the extra half of the name that got put into the data when the reader split the names of the countries that had commas in them
    del csv_list[25][1]
    del csv_list[50][1]
    del csv_list[73][1]
    del csv_list[85][1]
    del csv_list[91][1]
    del csv_list[101][1]
    del csv_list[112][1]
    del csv_list[126][1]
    del csv_list[147][1]
    del csv_list[159][1]
    del csv_list[195][1]
    del csv_list[249][1]
    del csv_list[256][1]
    del csv_list[258][1]

    return(csv_list, countries)



def get_dates(list_name):
    dates = list()
    for i in range(4,len(list_name[2])):
        dates.append(list_name[2][i])
    return dates

def combine_data_and_dates(countries, country, dataset, dates):
    index = countries.index(country)
    country_data = list()
    for m in range(4,len(dataset[index+3])):
        country_data.append(dataset[index+3][m])
        #country_data.append(dataset[index+3][m][1:-1])
    data_list = list()   
    for m in range(0,len(country_data)-2):
        #data_list.append([dates[m],country_data[m]])
        #this loop combines the data into a list of pairs
        #print([m,dates[m],country_data[m]])
        if not country_data[m]: #the if statement takes care of empty values
            data_list.append([float(dates[m]),country_data[m]])
        else:
            data_list.append([float(dates[m]),float(country_data[m])])
    return(data_list)



def make_json_file(csv_file1,csv_file2,csv_file3):
    csv_list1 = fix_country_names(csv_file1)[0]
    csv_list2 = fix_country_names(csv_file2)[0]
    csv_list3 = fix_country_names(csv_file3)[0]
    countries = fix_country_names(csv_file1)[1]
    # print(countries)
    dates = get_dates(csv_list1)


    dict_list = list()
    for country in countries:
        #make an empty dictionary titled "country_dict"
        country_dict = {}

        country_dict[csv_list1[3][2]] = combine_data_and_dates(countries, country, csv_list1, dates)
        country_dict[csv_list2[3][2]] = combine_data_and_dates(countries, country, csv_list2, dates)
        country_dict[csv_list3[3][2]] = combine_data_and_dates(countries, country, csv_list3, dates)
        country_dict["name"] = country
        #put the data with the countries in the dictionary
        dict_list.append(country_dict)

    json_array = json.dumps(dict_list)
    json_file = open("json_file.json","w")
    print(json_array, file=json_file)
    json_file.close()
    return(dict_list)

def convert_user_variables(user_variable):
    national_debt = "http://api.worldbank.org/v2/en/indicator/gc.dod.totl.gd.zs?downloadformat=excel"
    co2 = "http://api.worldbank.org/v2/en/indicator/en.atm.co2e.pc?downloadformat=excel"
    agriculture_value_added = "http://api.worldbank.org/v2/en/indicator/nv.agr.totl.zs?downloadformat=excel"
    tuberculosis = "http://api.worldbank.org/v2/en/indicator/sh.tbs.incd?downloadformat=excel"
    GDP = "http://api.worldbank.org/v2/en/indicator/ny.gdp.mktp.cd?downloadformat=excel"
    birth_rate = "http://api.worldbank.org/v2/en/indicator/sp.dyn.cbrt.in?downloadformat=excel"
    life_expectancy = "http://api.worldbank.org/v2/en/indicator/sp.dyn.le00.in?downloadformat=excel"

    if user_variable == "National Debt":
        variable_file = get_data(national_debt)
    if user_variable == "Carbon Dioxide Emissions":
        variable_file = get_data(co2)
    if user_variable == "Agricultural Value Added":
        variable_file = get_data(agriculture_value_added)
    if user_variable == "Incidence of Tuberculosis":
        variable_file = get_data(tuberculosis)
    if user_variable == "GDP":
        variable_file = get_data(GDP)
    if user_variable ==  "Birth Rate":
        variable_file = get_data(birth_rate)
    if user_variable == "Life Expectancy":
        variable_file == get_data(life_expectancy)
    return(variable_file)


def take_user_variables(variable1, variable2, variable3):
    file1 = convert_user_variables(variable1)
    file2 = convert_user_variables(variable2)
    file3 = convert_user_variables(variable3)
    make_json_file(file1, file2, file3)

v1 = form.getvalue('v1')
v2 = form.getvalue('v2')
v3 = form.getvalue('v3')

take_user_variables(v1, v2, v3)