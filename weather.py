from flask import Flask
from flask import render_template
from flask import request
# from src.python.main import getData
# import src.python.weatherData
# import src.python.key
# import src.python.hour as hour
# import src.python.AI.weather_classifier as weather_classifier
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/recommend')
def recommend():
    lon = request.args.get('lon')
    lat = request.args.get('lat')

    # weather_data = getData(lat, lon)
    # summary = weather_data.summary
    # icon = weather_data.icon
    # hours = weather_data.hours

    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)