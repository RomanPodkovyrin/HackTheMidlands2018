import csv
import random
import requests

# Darksky API handling
api_key = 'fddb1aa2d4034f6d105a0dd0defd9cd2'
lon = 52.478856
lat = -1.892302
api_url = 'https://api.darksky.net/forecast/%s/%f,%f,' % (api_key, lon, lat) 

# CSV Data Handling
datafile = open('synthetic_data.csv', mode='w') 
data_writer = csv.writer(datafile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# Data Generation Handling
initial_date = 1388577600 #01/01/2014 @ 12:00am (UTC)
for i in range (400):
    final_api_url = '%s%d' % (api_url, initial_date)
    r = requests.get(final_api_url)
    data = r.json()

    temp     = data['currently']['temperature']
    humidity = data['currently']['humidity']
    preci    = data['currently']['precipProbability']
    wind     = data['currently']['windSpeed']
    data_writer.writerow([initial_date, temp, humidity, preci, wind])

    print('writing information for ' + str([initial_date, temp, humidity, preci, wind]))
    
    # Get the data for the next day
    # This will ensure that we get data for the next 400 days
    # This means that all 4 seasons will be counted for
    initial_date = initial_date + (24*60*60)