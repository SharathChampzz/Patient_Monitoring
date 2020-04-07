from urllib.request import urlopen
from bs4 import BeautifulSoup


def getData(url):
    try:
        html = urlopen(url).read()
        soup = BeautifulSoup(html,'html5lib')
        print(soup.prettify())
##        div = soup.find('div')
##        print(div.text)
##        return div.text
    except Exception as e:
        print(e)

url2 = 'https://console.firebase.google.com/project/computernetworkproject-e3955/database/computernetworkproject-e3955/data/Patient/patient1'
url = 'https://computernetworkproject-e3955.firebaseio.com/'
getData(url2)
