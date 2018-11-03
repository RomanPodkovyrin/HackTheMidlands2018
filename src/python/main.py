from forecastiopy import *
from .weather_data import Weather_data

apy_key = 'fddb1aa2d4034f6d105a0dd0defd9cd2'
latitude = 52.478856
longitude = -1.892302
def main():

    myID = ForecastIO.ForecastIO(apy_key,latitude = latitude, longitude =longitude)

    current = FIOCurrently.FIOCurrently(myID)
    print ('Temperature: ', current.temperature, current.humidity)


main()