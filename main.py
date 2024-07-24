# check3
import requests
from dotenv import load_dotenv
import os
# loding env
load_dotenv()
# constant

URI = "http://api.weatherapi.com/v1/current.json"
token = os.getenv('token')
# configu...
def weather(city,lang='no'): 
  params = {
    'key': token,
    'q': city,
    'lang': lang,
    }
  # network reqesting
  res = requests.get(URI,params)
  # converting to json
  data = res.json()
  # if location not found error
  if 'error'in data:
    print('location not found!')
    return
  # desctring used full data
  forescast={
    'current':data['current']['temp_c'],
    'temp':data['current']['temp_f'],
    'state':data['location']['region'],
    'condition':data['current']['condition']['text']
  }
  print(forescast)

input_user=input('enter a city name:')
location_user=input('enter a code (en=english):')

weather(input_user,location_user)