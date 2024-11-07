import requests
from bs4 import BeautifulSoup
from refresh_compnent import accessKey as key

def urlToHtml(isp):
    try:
        html=requests.get(key.ispUrl[isp])#access site
    except requests.exceptions.ConnectionError:
        print('Server internet is down. The issue will notified to the the admin')
        exit()
    html=html.text
    html=BeautifulSoup(html,'html.parser')#html code
    return html