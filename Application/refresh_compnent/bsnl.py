from refresh_compnent import accessKey as key

def bsnl(data):
    # RE for cost: (0-9)*
    for value in data['cost']: 
            if not value.isdigit(): #checking the data is not a number
                data['cost'].remove(value)# removing other data except numbers in elemeets
    # RE for plan: ('Plan'+'FRC').'-'.(0-9)*
    #TODO PLAN data filter
    return data