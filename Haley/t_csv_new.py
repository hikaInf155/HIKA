"""This module changes our csv data into json format"""
import csv
csv_list=list()
with open('ans.csv', 'rt',encoding='utf8') as csvfile:
    spamreader = csv.reader(csvfile,delimiter=',', quotechar='"')
    for row in spamreader:
        csv_list.append(row)
countries = list()
print(csv_list)
for i in range(3,len(csv_list)):
    countries.append(csv_list[i][0])
    
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


dates = list()
for i in range(4,len(csv_list[2])):
    dates.append(csv_list[2][i])
                          
dict_list = list()
for i in range(0,len(countries)):
    #make an empty dictionary titled "country_dict"
    country_dict = {}

    #put the data with the countries in the dictionary

    country_data = list()
    for m in range(4,len(csv_list[i+3])):
        country_data.append(csv_list[i+3][m])
        #country_data.append(csv_list[i+3][m][1:-1])
    data_list = list()   
    for m in range(0,len(country_data)-1):
        #data_list.append([dates[m],country_data[m]])
        #this loop combines the data into a list of pairs
        print([m,dates[m],country_data[m]])
        if not country_data[m]: #the if statement takes care of empty values
            data_list.append([float(dates[m]),country_data[m]])
        else:
            data_list.append([float(dates[m]),float(country_data[m])])
    
    dict_list.append(country_dict)
    country_dict["data"] = data_list
    #put the names of the countries with the "name" key in the dictionary
    country_dict["name"] = countries[i] 

import json

json_array = json.dumps(dict_list)
json_file = open("json_file.json","w")
print(json_array, file=json_file)
json_file.close()
