import requests
url = input('Введіть адресу: ')


def get_response_from_web(url):
    rg = requests.get(url)
    rh = requests.head(url)
    ro = requests.options(url)
    print('REQUEST HEAD: ' + str(rh))
    print('REQUEST GET: ' + str(rg) + '\n')
    print('Request GET TEXT: \n' + rg.text.lstrip()[0:1000] + '\n')
    print('REQUEST OPTIONS: ' + str(ro))
    return rg.text

get_response_from_web(url)