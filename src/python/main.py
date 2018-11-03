from forecastiopy import *
from idna import unicode
from weather_data import Weather_data
from datetime import datetime

api_key = 'fddb1aa2d4034f6d105a0dd0defd9cd2'
latitude = 52.478856
longitude = -1.892302
myID =""

def main():
    global myID
    myID = ForecastIO.ForecastIO(api_key,
                                 units = ForecastIO.ForecastIO.UNITS_UK,
                                 lang = ForecastIO.ForecastIO.LANG_ENGLISH,
                                 latitude = latitude, longitude =longitude)

    current = FIOCurrently.FIOCurrently(myID)
    print ('Temperature: ', current.temperature, current.humidity)
    #populateWeatherDataClass(current)
    #getHourlyWeather()
    #getFlags()
    getCurrentWeather()

def populateWeatherDataClass(weatherTimeForecast):
    datalist= []

    datalist.append(weatherTimeForecast.apparentTemperature)
    datalist.append(weatherTimeForecast.pressure)
    datalist.append(weatherTimeForecast.cloudCover)
    datalist.append(weatherTimeForecast.dewPoint)
    datalist.append(weatherTimeForecast.humidity)
    datalist.append(weatherTimeForecast.precipIntensity)
    #datalist.append(weatherTimeForecast.)
    datalist.append(None)
    datalist.append(weatherTimeForecast.nearestStormDistance)
    #datalist.append(weatherTimeForecast.nearestStormDirection)
    datalist.append(None)
    datalist.append(weatherTimeForecast.ozone)
    #datalist.append(weatherTimeForecast.precipType)
    #datalist.append(weatherTimeForecast.snowfall)
    #datalist.append(weatherTimeForecast.sunRise)
    #datalist.append(weatherTimeForecast.sunSet)
    datalist.append(None)
    datalist.append(None)
    datalist.append(None)
    datalist.append(None)
    datalist.append(weatherTimeForecast.temperature)
    #datalist.append(weatherTimeForecast.textSummaries)
    datalist.append(None)
    datalist.append(weatherTimeForecast.uvIndex)
    datalist.append(weatherTimeForecast.windGust)
    datalist.append(weatherTimeForecast.windSpeed)
    #datalist.append(weatherTimeForecast.windDirection)
    datalist.append(None)

    print(datalist)
    #dataClass = Weather_data(datalist)


def getHourlyWeather():
    if myID.has_hourly() is True:

        hourly = FIOHourly.FIOHourly(myID)
        print(hourly.summary)

        for hour in range (0,hourly.hours()):
            print('Hour', hour+1)
            for item in hourly.get_hour(hour).keys():
                time=""
                if item == 'time':
                    time = datetime.utcfromtimestamp(hourly.get_hour(hour)[item]).strftime('%H:%M:%S %d-%m-%Y ')
                extra = "" + time
                print("   "+item + ':' + str(hourly.get_hour(hour)[item]) + " " + extra)
    else:
        print('No Hourly data'
              '')

def getFlags():
    if myID.has_flags() is True:
        from pprint import pprint
        flags = FIOFlags.FIOFlags(myID)
        pprint(vars(flags))
        # Get units directly
        print(flags.units)
    else:
        print('No Flags data')

def getCurrentWeather():
    if myID.has_currently() is True:
        currently = FIOCurrently.FIOCurrently(myID)
        print('Currently')
        for item in currently.get().keys():
            time = ""
            if item == 'time':
                time = datetime.utcfromtimestamp(currently.get()[item]).strftime('%H:%M:%S %d-%m-%Y ')
            extra = "" + time
            print(item + ' : ' + unicode(currently.get()[item]) + " " + extra)
        # Or access attributes directly
        print(currently.temperature)
        print(currently.humidity)
    else:
        print('No Currently data')
def getMinutalyWeather():
    pass
def getDailyWeather():
    pass

main()
