import requests
def my_weater(sit):
    api = '568517faa72b12b70cf0b2e4ab3b55e8'
    weat = requests.get('http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}'.format(sit,api))
    weat = weat.json()
    temp = ((weat.get('main')).get('temp')) - 273
    temper = (round(temp,1))
    return temper


