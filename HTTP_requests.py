import requests



def get_response_from_web():
    url = input('Введіть адресу: ')
    rh = requests.head(url)
    rg = requests.get(url)
    ro = requests.options(url)
    print('REQUEST HEAD: ' + str(rh))
    print('REQUEST GET: ' + str(rg) + '\n')
    print('Request GET TEXT: \n' + rg.text.lstrip()[0:500] + '\n')
    print('REQUEST OPTIONS: ' + str(ro))
    return rg.text

get_response_from_web()