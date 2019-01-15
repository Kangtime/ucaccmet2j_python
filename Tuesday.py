import json

Seattle = []

with open('precipitation.json', encoding = 'utf-8-sig') as file:
    precipitation = json.load(file)
    for line in precipitation:
        if line['station'] == 'GHCND:US1WAKG0038':
            Seattle.append(line)
#print(Seattle)
for line in Seattle:
    del[line['datatype']]
    del[line['station']]
    line['year'], line['month'], line['day'] = line['date'].split("-")
    del[line['date']]
    del[line['year']]
    del[line['day']]
Seattle_month = [0]*12
for line in Seattle:
    months = int(line['month'])
    Seattle_month[months-1] = line['value'] + Seattle_month[months-1]
print(Seattle_month)


#print(Seattle)



   # for data in precipitation:
    #    if 'station' == 'GHCND:US1WAKG0038'

