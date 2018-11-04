# Weather App
Hack The Midlands 3.0

## Setting up the dependencies
### Flask
In order to run the server you need to have Flask installed.

```bash
pip3 install flask
```

To run the server (Python 3) you can run
```bash
python3 -m flask run
``` 
or you can run the app directly through
```bash
python3 weather.py
```

### Darksky and ForecastIO
To set up python Weather API go [here ](https://github.com/bitpixdigital/forecastiopy3/tree/bb8f7ca85f4ec9c0b8f6bab2da4c1396aa55d753)

clone it and run 
``` bash 
python setup.py install
```

###Run
run 
```python
weather.py
```
then open 
http://localhost:5000/