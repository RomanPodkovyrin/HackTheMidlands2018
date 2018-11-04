from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/recommend')
def recommend():
    lon = request.args.get('lon')
    lat = request.args.get('lat')
    
    return ' Latitude: %s | Longitude: %s' % (lat, lon)

if __name__ == '__main__':
    app.run(debug=True)