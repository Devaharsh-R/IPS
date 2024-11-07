from refresh_compnent import urlToHtml as uth
from refresh_compnent import htmlToData as htd
from refresh_compnent import accessKey as key
from refresh_compnent import filterData as fd

def getData(isp):
    html = uth.urlToHtml(isp)
    dataKey = key.accessKey[isp]
    data = htd.htmlToData(html,dataKey)
    refreshedData = fd.filterData(isp,data)
    return refreshedData