import requests as re
from bs4 import BeautifulSoup
# This is bsnl retreival only
response=re.get('https://www.bsnl.co.in/opencms/bsnl/BSNL/services/mobile/prepaid_plans_100822.html')
html=response.text
html=BeautifulSoup(html,'html.parser')#html code
cost=html.select('tr.table_conn')[0].text
cost=cost.split('\n')
cost = list(filter(None, cost))
cost = [el.replace('\xa0','') for el in cost] #reomoving uncode
cost = [el.replace(' ','') for el in cost]#The list become cost only
for value in cost:
    if not value.isdigit():
        cost.remove(value)
print(cost.__len__())
print(cost)
# TODO Take all the wanted data from the site