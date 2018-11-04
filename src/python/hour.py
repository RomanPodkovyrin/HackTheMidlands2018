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
            feel = "It's Cold. Dress warmly. Take 3 layers maybe?"
        elif self.layer == 1:
            feel = "It's FREEZING. Dress extra warmly. 4 layers minimum."
        elif self.layer == 2:
            feel = "The weather's alright to be fair. You can dress with 2 layers."
        elif self.layer == 3:
            feel = "It's quite warm. Wear 1-2 layers at most."
        elif self.layer == 4:
            feel = "Oof ow it's hot. Just wear a t-shirt and shorts."

        #return    "\nTime: " + str(self.time) +"    Layer: " +str(feel) +  "\n    precipIntensity: "+  str(self.precipIntensity) + "\n    precipProbability: " + str(self.precipProbability) + "\n    Temperature: " + str(self.temperature) +"\n    Humidity: " + str(self.humidity) + "\n    WindSpeed: " + str(self.windSpeed)
        return '\nTime:  '+ str(self.time) + '   Recommendation: ' +str(feel)
