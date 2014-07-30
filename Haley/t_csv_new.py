"""This module changes our csv data into json format"""
import csv
import json
import os
#os.chdir("C://Users//HaleyPC//Documents//HIKA//Haley")

def fix_country_names(file_name):
    
    csv_list=list()
    with open(file_name, 'rt',encoding='utf8') as csvfile:
        spamreader = csv.reader(csvfile,delimiter=',', quotechar='"')
        for row in spamreader:
            csv_list.append(row)
    countries = list()
    #print(csv_list)
    for i in range(3,len(csv_list)):
        countries.append(csv_list[i][0])

    #make names of data easier

    if csv_list[3][2] == "CO2 emissions (metric tons per capita)":
        csv_list[3][2] = "CO2"
    if csv_list[3][2] == "Agriculture, value added (% of GDP)":
        csv_list[3][2] = "Agriculture"
    if csv_list[3][2] == "Incidence of tuberculosis (per 100,000 people)":
        csv_list[3][2] = "Tuberculosis"
    
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

make_json_file('co2_data.csv',"agr_data.csv","tuber_data.csv")
