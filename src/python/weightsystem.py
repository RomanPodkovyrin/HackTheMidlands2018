#from numpy.random import choice
#elements = ['one', 'two', 'three'] 
#weights = [0.2, 0.3, 0.5]
#print(choice(elements, p=weights))


# Python class
# Use methods for the weights of each weather
# Call final method do collect the weights
# Use numpy to choose the weather

# preceipInts -> precipIntensity
# precipProb -> precipProbability
# precipAcc -> precipAccumulation
class WeightSystem:
    # High humidity - 90, low humidity - 70
    def __init__(self, windSpeed, precipInts, precipType, precipAcc, precipProb, nearestStormDistance, temperature, uvIndex, humidity):

        
        # Cold air with high humidity feels colder
        # Hot with high humidity feels hotter
        self.humidity = humidity
        self.windSpeed = windSpeed
        self.precipType = precipType
        self.precipInts = precipInts
        self.precipProb = precipProb
        self.nearestStormDistance = nearestStormDistance
        self.temperature = temperature
        # Initial weights for the weather
        self.sunWeight = 0
        self.coldWeight = 0
        self.snowWeight = 0
        self.rainWeight = 0
        self.windWeight = 0
        # Dictionary to keep track of the weights of the weather
        self.weatherDictionary = {"Sun":self.sunWeight, "Cold":self.coldWeight, "Snow":self.snowWeight, "Rain":self.rainWeight, "Wind":self.windWeight}
        
       

    # If statement based weighting calculation
    def sunWeightCalc(self):
        # It is cold if temperature is less than 59, otherwise its most likely to be hot
        if self.temperature >= 59:
            self.weatherDictionary["Sun"] += 1
            
        if self.temperature >= 59:
           self.weatherDictionary["Sun"] += 1
        
        
    
    def coldWeightCalc(self):
        if self.temperature >= 59:
            self.weatherDictionary["Cold"] += 1
            self.weatherDictionary["Snow"] += 1
           
    def snowWeightCalc(self):
        # Check precipIntensity is present?
        if (self.precipType == "snow") or (self.precipType == "sleet"):
            self.weatherDictionary["Snow"] += 1
        if self.precipProb > 0.5:
            self.weatherDictionary["Snow"] += 0.5
            
            
    def rainWeightCalc(self):
        if self.precipType == "rain":
            self.weatherDictionary["Rain"] += 1
           
        if self.nearestStormDistance < 20:
            self.weatherDictionary["Rain"] += 1
        if self.precipProb > 0.5:
            self.weatherDictionary["Rain"] += 1
            self.weatherDictionary["Cold"] += 0.5
           
    def windWeightCalc(self):
        if self.nearestStormDistance < 20:
            self.weatherDictionary["Wind"] += 1
           

        if self.windSpeed > 25:
            self.weatherDictionary["Wind"] += 1
           

    

    # Function to process the weights
    def processWeights(self):
        self.sunWeightCalc()
        self.coldWeightCalc()
        self.snowWeightCalc()
        self.rainWeightCalc()
        self.windWeightCalc()

    # Get the weather condition based on the weights
    


    # Methods to get the value of the weights
    def getSunWeight(self):
        return (self.sunWeight,"sun")
    def getColdWeight(self):
        return (self.coldWeight, "cold")
    def getSnowWeight(self):
        return (self.snowWeight, "snow")
    def getRainWeight(self):
        return (self.rainWeight, "rain")
    def getWindWeight(self):
        return (self.windWeight, "wind")
    

    # Methods to reset all weights
    def resetWeights(self):
        self.sunWeight = 0
        self.coldWeight = 0
        self.snowWeight = 0
        self.rainWeight = 0
        self.windWeight = 0

    def getDictionary(self):
        return self.weatherDictionary
    def getWeather(self):
        weatherList = []
        for key, value in weights.getDictionary().items():
            if value == (max(weights.getDictionary().values())):
                weatherList.append(key)
        return weatherList
        
   
# Initiate the weight class
weights = WeightSystem(16.09, 0, "rain", None, 0.01, 60, 55.4, 1, 0.73)
# Calculate all weights for probability of Snow, Rain, Sun, Wind, Cold
weights.processWeights()
#  Returns a list of the weather(s) with the highest weighting
print(weights.getWeather())





