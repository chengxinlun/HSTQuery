import json


def hscResultPreparser(filename):
    '''
    Preparse json file since the saved one only has one line
    '''
    upFile = open(filename)
    upData = upFile.read()
    upFile.close()
    pData = str.split(upData, ']')
    return pData


def hscResultParser(pData):
    keepData = []
    for each in pData:
        if each != '':
            tmp = each + ']'
            tmpData = json.loads(tmp)
            keepData.append(tmpData[0])
    return keepData
