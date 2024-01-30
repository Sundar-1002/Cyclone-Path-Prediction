import requests
import csv

response = requests.get("https://eonet.gsfc.nasa.gov/api/v3/categories/severeStorms")

c = csv.writer(open("myvalues.csv","w"), lineterminator="\n")

i = 0
r = response.json()
print(response.status_code)
headerList = ['CycloneName','DateTime','Type','Latitude','Longitude','Maximum Wind']
c.writerow(headerList)
s = len(r['events'])
for k in range(0,s):
   title = r['events'][k]['title']
   print(r['events'][k]['title'])


for j in range(0,s):
   for item in r['events'][j]['geometry']:
      print(item)
      print(j) 
      c.writerow([r['events'][j]['title'],r['events'][j]['geometry'][i]['date'],r['events'][j]['geometry'][i]['type'],r['events'][j]['geometry'][i]['coordinates'][1],r['events'][j]['geometry'][i]['coordinates'][0],r['events'][j]['geometry'][i]['magnitudeValue']])
      i=i+1


