# bsnl data retreval.
import requests as re
from bs4 import BeautifulSoup
response=re.get('https://www.bsnl.co.in/opencms/bsnl/BSNL/services/mobile/prepaid_plans_100822.html')
op=response.text
content=BeautifulSoup(op).text
words=content.split('\n')
print(words)