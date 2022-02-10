import json
from posixpath import split
file = open('countries.json', 'r')
data = file.read()

countries = json.loads(data)

countriesCode = []
countriesName = []

for i in countries:   
    countriesCode+= i['alpha2'].split('\n')
    countriesName += i['name'].split('\n')

print(countriesCode[1])
print(countriesName[1])