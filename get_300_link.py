import requests
s_url = input('Enter shortener URL(Example: https://bit.ly/37W7bWy, https://goo.gl/vLfoaW): ').strip()

def get_url_from_shortener(s_url):
    r = requests.get(s_url)
    print("STATUS CODE OF SHORTENER: " +str(r.status_code))
    print("STATUS CODE IN REQUEST HISTORY: " + str(r.history))
    fullurl = r.url
    return fullurl

f_url = get_url_from_shortener(s_url)
print('FULL URL FROM THE PROVIDED SHORTENER LINK: \n' + f_url)
