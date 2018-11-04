class Hour:
    def __init__ (self,layer,time,precipIntensity,
                  precipProbability,temperature,humidity,
                  windSpeed):
        #['COLD', 'OK', 'FREEZING', 'WARM', 'HOT']
        #   0   ,  1  ,     2     ,   3   ,   4
        self.layer             = layer
        self.time              = time
        self.precipIntensity   = precipIntensity
        self.precipProbability = precipProbability
        self.temperature       = temperature
        self.humidity          = humidity
        self.windSpeed         = windSpeed
        #self.uvIndex          =

