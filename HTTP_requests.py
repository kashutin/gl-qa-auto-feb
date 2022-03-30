import requests



def get_response_from_web():
    url = input('Введіть адресу: ')
    rh = requests.head(url)
    rg = requests.get(url)
    ro = requests.options(url)
    print(rh)
    print('Request GET TEXT: \n' + rg.text.lstrip()[0:500])
    print(rg)
    print(ro)
    return rg

get_response_from_web()