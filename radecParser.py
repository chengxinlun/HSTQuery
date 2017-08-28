def raParser(raStr):
    tmp = raStr.split(' ')
    hr = float(tmp[0]) + float(tmp[1]) / 60.0 + float(tmp[2]) / 3600.0
    return hr * 15.0


def decParser(decStr):
    tmp = decStr.split(' ')
    if decStr.startswith('+'):
        deg = float(tmp[0]) + float(tmp[1]) / 60.0 + float(tmp[2]) / 3600.0
    else:
        deg = float(tmp[0]) - float(tmp[1]) / 60.0 - float(tmp[2]) / 3600.0
    return deg


def raKeyFinder(keys):
    for each in keys:
        if "RA" in each:
            return each
    raise Exception("No key with 'RA' substring found")


def decKeyFinder(keys):
    for each in keys:
        if "Dec" in each:
            return each
    raise Exception("No key with 'RA' substring found")
