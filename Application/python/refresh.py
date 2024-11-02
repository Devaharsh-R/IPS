import requests as re
from bs4 import BeautifulSoup
# This is bsnl retreival only
response=re.get('https://www.bsnl.co.in/opencms/bsnl/BSNL/services/mobile/prepaid_plans_100822.html')
html=response.text
content=BeautifulSoup(html,'html.parser')#html code
cost=content.select('tr.table_conn')[0].text
print(cost)
# TODO Remove unwanted data from the list