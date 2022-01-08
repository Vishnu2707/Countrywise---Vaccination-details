#if u need the data for a particular state, uncomment and comment the other print statements.

import requests

URL = 'https://disease.sh/v3/covid-19/gov/India'

r = requests.get(URL)

data = r.json()

states = data['states']

#inp = input("Enter the name of the state to get covid updates!!\n")

for i in range(len(states)):

    p = states[i]

    # if(p['state'].lower()==inp.lower()):
        # print("-----------------------------------------------------------------------")
        # print("\nState - ",p['state'],"\nActive cases - ",p['active'],"\nRecovered - ",p['recovered'],"\nDeaths - ",p['deaths'],"\nToday's total cases -",p['todayCases'])
        # print("\n-----------------------------------------------------------------------")

    print("-----------------------------------------------------------------------")
    print("\nState - ",p['state'],"\nActive cases - ",p['active'],"\nRecovered - ",p['recovered'],"\nDeaths - ",p['deaths'],"\nToday's total cases -",p['todayCases'])
    print("\n-----------------------------------------------------------------------")