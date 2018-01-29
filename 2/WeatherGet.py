import requests
import sys
length = len(sys.argv)
if length == 2:
  city = sys.argv[1]
  uri = 'https://api.openweathermap.org/data/2.5/weather'
  r = requests.get(uri, params = {'q':city, 'appid':'c01da1b70aeae026480c40cc5806d322', 'units':'metric'}).text
  print(r)
else:
  print('Incorrect amount of parameters:',  length-1, '. Example of correct parameters: python WeatherGet.py Larnaca')
