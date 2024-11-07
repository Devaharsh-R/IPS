from refresh_compnent import getData as gd
import sys

ispName = sys.argv[1]
refreshedData=gd.getData(ispName)
for key in refreshedData:
    print('\n\n',key,' : ',refreshedData[key])
# TODO Take all the wanted data from the site