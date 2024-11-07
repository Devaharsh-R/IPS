def htmlToData(html,key):
    allData={} # a dictionary is declared
    for selector in key:
        try:
          data=html.select(key[selector])[0].text # taking specific data as string
        except IndexError:
            print('ISP Web site is modified. We cannot refresh the data due to this modification. You can access the modified page only changes made by the admin. Do you want to continue with the old web ?')
            exit()
        data = data.split('\n') # seperating data with list
        data = list(filter(None, data)) # removing emplty elements
        data = [el.replace('\xa0','') for el in data] #reomoving unicode
        data = [el.replace(' ','') for el in data]#removing unwanted spaces in elements
        allData[selector]=data # inserting selector as key of dictionary and and list as value. Appending while iterating.
    return allData 