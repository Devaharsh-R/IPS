from refresh_compnent import bsnl as isp1

def filterData(isp,data):
    if isp == 'bsnl':
        filteredData = isp1.bsnl(data)
    return filteredData