import requests



def get_html_from_web():
    url = input('Введіть адресу: ')
    response = requests.get(url)
    print(response.status_code)
    print(response.text[0:500])
    return response.text