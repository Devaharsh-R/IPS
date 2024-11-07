# from refresh_compnent import accessKey as key
import re #regex

def bsnl(data):
    filteredContent={}
    # RE for cost: (0-9)*
    temp=[] # empty list for cost
    for value in data['content']: 
            if  value.isdigit(): #checking the data is not a number
                temp.append(value) # inserting cost value to list
    filteredContent['cost']=temp # inserted the list
    # RE for plan: ('Plan'+'FRC').'-'.(0-9)*
    temp=[] # empty list for 
    pattern=r'(Plan|FRC)-\d*'
    for value in data['heading']:
         temp=re.findall(pattern,value)
    #FIXME PLAN data filter
    filteredContent['plan']=temp
    return filteredContent