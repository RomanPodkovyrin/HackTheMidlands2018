class WeatherData:
    def __init__(self, summary, icon, data):
        self.summary =  summary
        self.icon = icon
        self.hours = data #array

    def getReport(self):
        stuff = ""
        for hour in self.hours:
            stuff = stuff + "\n" +hour.getString()

        return str(self.summary) +"\n" + stuff
