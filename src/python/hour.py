from datetime import datetime
class Hour:
    def __init__ (self,layer,time,precipIntensity,
                  precipProbability,temperature,humidity,
                  windSpeed):
        #['COLD', 'FREEZING', 'OK', 'WARM', 'HOT']
        #   0   ,  1  ,     2     ,   3   ,   4
        self.layer             = layer
        self.time              = datetime.utcfromtimestamp(time).strftime('%H:%M:%S %d-%m-%Y ')
        self.precipIntensity   = precipIntensity
        self.precipProbability = precipProbability
        self.temperature       = temperature
        self.humidity          = humidity
        self.windSpeed         = windSpeed
        #self.uvIndex          =
    def getString(self):
        feel = ""
        if self.layer == 0 :
            feel = "Cold"
        elif self.layer == 1:
            feel = "Freezing"
        elif self.layer == 2:
            feel = "Ok"
        elif self.layer == 3:
            feel = "Warm"
        elif self.layer == 4:
            feel = "Hot"

        return    "\nTime: " + str(self.time) +"    Layer: " +str(feel) +  "\n    precipIntensity: "+  str(self.precipIntensity) + "\n    precipProbability: " + str(self.precipProbability) + "\n    Temperature: " + str(self.temperature) +"\n    Humidity: " + str(self.humidity) + "\n    WindSpeed: " + str(self.windSpeed)

