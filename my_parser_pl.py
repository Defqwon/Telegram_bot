import requests
def waluta():
    dol = requests.get('https://api.nbp.pl/api/exchangerates/rates/c/usd/last/1/?format=json')
    eur = requests.get('https://api.nbp.pl/api/exchangerates/rates/c/eur/last/1/?format=json')
    dol = dol.json()
    eur = eur.json()
    itog = []
    itog.append((dol.get('rates')[0]).get('bid'))
    itog.append((dol.get('rates')[0]).get('ask'))
    itog.append((eur.get('rates')[0]).get('bid'))
    itog.append((eur.get('rates')[0]).get('ask'))

    return itog
