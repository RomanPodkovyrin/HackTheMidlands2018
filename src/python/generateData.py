import csv
import random
import requests
from decimal import Decimal
import key

# Darksky API handling
#api_key = 'fddb1aa2d4034f6d105a0dd0defd9cd2'
api_key = key.getKey()
latitude,longitude = key.getLocation()
api_url = 'https://api.darksky.net/forecast/%s/%f,%f,' % (api_key, latitude,longitude)

# CSV Data Handling
datafile = open('synthetic_data.csv', mode='w') 
data_writer = csv.writer(datafile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


# Aux functions
def tempFtoC(fahrenheit):
    return ( (fahrenheit - 32) / 1.8)

# Data Generation Handling
initial_date = 1388577600 #01/01/2014 @ 12:00am (UTC)
for i in range (400):
    final_api_url = '%s%d' % (api_url, initial_date)
    r = requests.get(final_api_url)
    data = r.json()

    temp     = data['currently']['temperature']
    temp     = round(tempFtoC(temp),2)
    humidity = data['currently']['humidity']
    preci    = data['currently']['precipIntensity']
    wind     = data['currently']['windSpeed']
    data_writer.writerow([ temp, humidity, preci, wind])

    print( str(i) + ': writing information for ' + str([initial_date, temp, humidity, preci, wind]))
    
    # Get the data for the next day
    # This will ensure that we get data for the next 400 days
    # This means that all 4 seasons will be counted for
    initial_date = initial_date + (24*60*60)

