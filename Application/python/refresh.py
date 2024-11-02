import requests as re
from bs4 import BeautifulSoup
# This is bsnl retreival only
response=re.get('https://www.bsnl.co.in/opencms/bsnl/BSNL/services/mobile/prepaid_plans_100822.html')
html=response.text
content=BeautifulSoup(html,'html.parser')#html code
cost=content.select('tr.table_conn')[0].text
cost=cost.split('\n')
cost = list(filter(None, cost))
cost = [el.replace('\xa0',' ') for el in cost]
for value in cost:
    if not value.isdigit():
        cost.remove(value) #FIXME some wanted values are removed
print(cost)
# TODO Take all the wanted data from the