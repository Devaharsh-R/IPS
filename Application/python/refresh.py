import requests as re
from bs4 import BeautifulSoup
response=re.get('https://www.bsnl.co.in/opencms/bsnl/BSNL/services/mobile/prepaid_plans_100822.html')
# This is bsnl retreival only
op=response.text
content=BeautifulSoup(op,'html.parser').text
words=content.split('\n')
words = list(filter(None, words))
print(words)
# TODO Remove unwanted data from the list