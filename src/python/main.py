from forecastiopy import *
from idna import unicode
import csv
from datetime import datetime
from hour import Hour
from weatherData import WeatherData
import key

#api_key = 'fddb1aa2d4034f6d105a0dd0defd9cd2'
#api_key =
api_key = key.getKey()
latitude = 52.478856
longitude = -1.892302
myID =""

def main():
    #getHourlyWeather()
    #getFlags()
    #getCurrentWeather()
    #getMinutalyWeather()
    #getDailyWeather()
    getData()

def setup():
    global myID , latitude,longitude

    latitude, longitude = key.getLocation()

    myID = ForecastIO.ForecastIO(api_key,
                                 units=ForecastIO.ForecastIO.UNITS_UK,
                                 lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                                 latitude=latitude, longitude=longitude)
def getData():

    setup()
    if myID.has_hourly() is True:
        hourly = FIOHourly.FIOHourly(myID)
        #print(hourly.summary)
        summary = hourly.summary
        #print(hourly.icon)
        icon = hourly.icon
        hours = []
        for hour in range (0,hourly.hours()):
            print('Hour', hour+1)
            time = hourly.get_hour(hour)["time"]
            precipIntensity = hourly.get_hour(hour)["precipIntensity"]
            precipProbability = hourly.get_hour(hour)["precipProbability"]
            temperature = hourly.get_hour(hour)["temperature"]
            humidity = hourly.get_hour(hour)["humidity"]
            windSpeed = hourly.get_hour(hour)["windSpeed"]
            layer = predict(temperature,humidity,precipIntensity,windSpeed)
            hour = Hour(layer, time,precipIntensity,
                        precipProbability,temperature,
                        humidity,windSpeed)
    else:
        print('No Hourly data')

    weather = WeatherData(None,None,None)

    return weather

def predict():
    pass



def getHourlyWeather():
    if myID.has_hourly() is True:

        hourly = FIOHourly.FIOHourly(myID)
        print(hourly.summary)
        print(hourly.icon)

        for hour in range (0,hourly.hours()):
            print('Hour', hour+1)
            for item in hourly.get_hour(hour).keys():
                time=""
                if item == 'time':
                    time = datetime.utcfromtimestamp(hourly.get_hour(hour)[item]).strftime('%H:%M:%S %d-%m-%Y ')
                extra = "" + time
                print("   "+item + ':' + str(hourly.get_hour(hour)[item]) + " " + extra)
    else:
        print('No Hourly data')

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
            print("   "+item + ' : ' + unicode(currently.get()[item]) + " " + extra)
        # Or access attributes directly
        print(currently.temperature)
        print(currently.humidity)
    else:
        print('No Currently data')
def getMinutalyWeather():
    if myID.has_minutely() is True:
        minutely = FIOMinutely.FIOMinutely(myID)
        print('Minutely')
        print('Summary:', minutely.summary)
        print('Icon:', minutely.icon)

        for minute in range(0, minutely.minutes()):
            print('Minute', minute + 1)
            for item in minutely.get_minute(minute).keys():
                time = ""
                if item == 'time':
                    time = datetime.utcfromtimestamp(minutely.get_minute(minute)[item]).strftime('%H:%M:%S %d-%m-%Y ')
                extra = "" + time
                print("   "+item + ' : ' + unicode(minutely.get_minute(minute)[item]) + " " + extra)

            # Or access attributes directly for a given minute.
            # minutely.minute_3_time would also work
            print(minutely.minute_1_time)
    else:
        print('No Minutely data')
def getDailyWeather():
    if myID.has_daily() is True:
        daily = FIODaily.FIODaily(myID)
        print('Daily')
        print('Summary:', daily.summary)
        print('Icon:', daily.icon)

        for day in range(0, daily.days()):
            print('Day', day + 1)
            for item in daily.get_day(day).keys():
                time = ""
                if item == 'time':
                    time = datetime.utcfromtimestamp(daily.get_day(day)[item]).strftime('%H:%M:%S %d-%m-%Y ')
                extra = "" + time
                print("   "+item + ' : ' + str(daily.get_day(day)[item]) + " " + extra)
            # Or access attributes directly for a given minute.
            # daily.day_7_time would also work
            print(daily.day_5_time)
    else:
        print('No Daily data')


main()
