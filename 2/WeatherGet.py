import requests
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('City', help= 'Use city name as an argument')
city = parser.parse_args().City
uri = 'https://api.openweathermap.org/data/2.5/weather'
r = requests.get(uri, params = {'q':city, 'appid':'c01da1b70aeae026480c40cc5806d322', 'units':'metric'}).text
print(r)

