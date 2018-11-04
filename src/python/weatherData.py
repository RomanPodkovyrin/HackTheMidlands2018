class WeatherData:
    def __init__(self, summary, icon, data):
        self.summary =  summary
        self.icon = icon
        self.hours = data #array

    def getReport(self):
        umb = ""
        stuff = ""
        for hour in self.hours:
            stuff = stuff + "\n" +hour.getString()
            if hour.precipProbability > 0.4:
                umb = "   Take an umbrella"

        return str(self.summary) +"\n" + stuff  + umb
