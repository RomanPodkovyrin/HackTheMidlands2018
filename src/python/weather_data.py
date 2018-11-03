class Weather_data:

    '''
    def __init__(self, apparentTemperature,pressure,cloudCover,dewPoint,humidity
                 ,liquid_precipitation_rate,nearestStormDistance,nearest_storm_direction
                 ,ozone,precipType,snowfall,sun_rise,sun_set,temperature,text_summaries
                 ,uvIndex,windGust,windSpeed,windDirection):
        self.apparentTemperature = apparentTemperature
        self.pressure = pressure
        self.cloudCover = data[2]
        self.dewPoint = data[3]
        self.humidity = data[4]
        self.liquid_precipitation_rate = data[5]
        self.nearestStormDistance = data[7]
        self.nearest_storm_direction = data[8]
        self.ozone = data[9]
        self.precipType = data[10]
        self.snowfall = data[11]
        self.sun_rise = data[12]
        self.sun_set = data[13]
        self.temperature = data[14]
        self.text_summaries = data[15]
        self.uvIndex = data[16]
        self.windGust = data[17]
        self.windSpeed = data[18]
        self.windDirection = data[19]'''
    def __init__(self, data):
        self.apparentTemperature       = data[0]
        self.pressure                  = data[1]
        self.cloudCover                = data[2]
        self.dewPoint                  = data[3]
        self.humidity                  = data[4]
        self.liquid_precipitation_rate = data[5]
        self.moon_phase                = data[6]
        self.nearestStormDistance      = data[7]
        self.nearest_storm_direction   = data[8]
        self.ozone                     = data[9]
        self.precipType                = data[10]
        self.snowfall                  = data[11]
        self.sun_rise                  = data[12]
        self.sun_set                   = data[13]
        self.temperature               = data[14]
        self.text_summaries            = data[15]
        self.uvIndex                   = data[16]
        self.windGust                  = data[17]
        self.windSpeed                 = data[18]
        self.windDirection             = data[19]

