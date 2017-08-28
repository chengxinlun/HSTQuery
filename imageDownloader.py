import os
import urllib


def imageDownloader(ra, dec, imageName, targetName, zoom, formatCode, pixel,
                    saveDir):
    fileName = os.path.join(saveDir, targetName + '.' + formatCode)
    baseUrl = "http://hla.stsci.edu/cgi-bin/fitscut.cgi?"
    redQuery = "red=" + imageName + "&"
    raQuery = 'RA=' + str(ra) + "&"
    decQuery = 'Dec=' + str(dec) + "&"
    zoomQuery = 'zoom=' + str(zoom) + '&'
    sizeQuery = 'size=' + str(pixel) + '&'
    formatQuery = 'Format=' + formatCode + '&Download=1'
    downloadUrl = baseUrl + redQuery + raQuery + decQuery + zoomQuery + \
        sizeQuery + formatQuery
    urllib.URLopener()
    urllib.urlretrieve(downloadUrl, fileName)
