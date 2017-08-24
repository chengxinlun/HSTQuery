from hscResultParser import hscResultPreparser, hscResultParser


hscData = hscResultParser(hscResultPreparser('../hsc_search.json'))
print("Found " + str(len(hscData)) + " entries")
