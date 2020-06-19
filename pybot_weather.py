import requests

def weather_command():
    base_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    city_code = '130010'
    url = '{}?city={}'.format(base_url, city_code)
    r = requests.get(url)
    weather_date = r.json()
    city = weather_date['location']['city']
    label = weather_date['forecasts'][0]['dateLabel']
    telop = weather_date['forecasts'][0]['telop']

    response = '{}の{}の天気は{}です。'.format(city, label, telop)
    return response
