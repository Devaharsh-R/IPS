from refresh_compnent import getData as gd
import sys

ispName = sys.argv[1]
refreshedData=gd.getData(ispName)
print(refreshedData['cost'].__len__())
print(refreshedData['cost'])
# TODO Take all the wanted data from the site