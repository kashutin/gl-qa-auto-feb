import requests
url = input('Введіть адресу(bit.ly, goo.gl, etc): ')

def recieve_url_from_shortener(url):
    r = requests.get(url)
    print("STATUS CODE OF SHORTENER: " +str(r.status_code))
    print("STATUS CODE IN REQUEST HISTORY: " + str(r.history))
    fullurl = r.url
    return fullurl
full_url = recieve_url_from_redirect(url)
print('FULL URL FROM PROVIDED LINK: \n' + full_url)
