import urllib


def imageDownloader(ra, dec, imageName, targetName):
    fileName = targetName + '.fits'
    baseUrl = "http://hla.stsci.edu/cgi-bin/fitscut.cgi?"
    redQuery = "red=" + imageName + "&"
    raQuery = 'RA=' + str(ra) + "&"
    decQuery = 'Dec=' + str(dec) + "&"
    zoomQuery = 'zoom=1.0&'
    formatQuery = 'Format=fits&Download=1'
    downloadUrl = baseUrl + redQuery + raQuery + decQuery + zoomQuery + \
        formatQuery
    urllib.URLopener()
    urllib.urlretrieve(downloadUrl, fileName)
