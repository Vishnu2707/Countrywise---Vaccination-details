import requests

URL = 'https://disease.sh/v3/covid-19/vaccine/coverage/countries?lastdays=1'

r = requests.get(URL)

data = r.json()

# For getting the vaccination details of all the countries, uncomment.
# for i in range (len(data)):

#     d = data[i]

#     country = d['country']

#     timeline = d['timeline']

#     for key,value in timeline.items():

#         print("\n Country : ",country,"\n","Last updated date : ",key,"\n","Total number of people vaccinated : ",value,"\n")
#         print("\n---------------------------------------------------------------")
x = input("Please enter the country name\n").lower()
ans = ""
flag=0
 
for i in range (len(data)):

    d = data[i]

    country = d['country']

    timeline = d['timeline']

    if country.lower() == x:

        ans = ans + country

        flag=flag+1

        break

if flag == 0:

    print('Enter a valid country name!!')

else:

    for key,value in timeline.items():

       print("\n Country : ",country,"\n","Last updated date : ",key,"\n","Total number of people vaccinated : ",(format(value, ",")),"\n") 



