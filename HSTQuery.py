from hscResultParser import hscResultPreparser, hscResultParser
from radecParser import raParser, decParser
from imageDownloader import imageDownloader


hscData = hscResultParser(hscResultPreparser('../hsc_search.json'))
print("Found " + str(len(hscData)) + " entries")
for each in hscData:
    ra = raParser(each['MatchRA(J2000)'])
    dec = decParser(each['MatchDec(J2000)'])
    imageDownloader(ra, dec, each['ImageName'], each['Target Name'])
