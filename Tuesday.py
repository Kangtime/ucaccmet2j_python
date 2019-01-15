import json

Seattle = []
#Switching JSON into file, separating all data from Seattle
with open('precipitation.json', encoding = 'utf-8-sig') as file:
    precipitation = json.load(file)
    for line in precipitation:
        if line['station'] == 'GHCND:US1WAKG0038':
            Seattle.append(line)
#Getting rid of unnecessary information about Seattle
for line in Seattle:
    del[line['datatype']]
    del[line['station']]
    line['year'], line['month'], line['day'] = line['date'].split("-")
    del[line['date']]
    del[line['year']]
    del[line['day']]
#Adding all the values for Seattle by month
Seattle_month = [0]*12
for line in Seattle:
    months = int(line['month'])
    Seattle_month[months-1] = line['value'] + Seattle_month[months-1]
print(Seattle_month)
#Making JSON of all the data
with open('Seattle.json', 'w') as file:
    json.dump(Seattle_month, file, indent=4, sort_keys=True)
print(Seattle_month)



#Part 2
#summing up all the values of all months
year_sum = int(sum(Seattle_month))
print(year_sum)

#taking the percentage of month compared to year
for i in Seattle_month:
    percentage = i*100/year_sum
    print(percentage)


#Part 3

