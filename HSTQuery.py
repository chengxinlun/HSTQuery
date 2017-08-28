import argparse
import errno
import os
import numpy as np
from astropy.io import fits
from hscResultParser import hscResultPreparser, hscResultParser
from radecParser import raParser, decParser, raKeyFinder, decKeyFinder
from imageDownloader import imageDownloader


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def setArg(argument, defValue):
    if argument is not None:
        return argument
    else:
        return defValue


if __name__ == '__main__':
    # Commandline argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("jsonFile", help='Input jason file from HSC search',
                        type=str)
    parser.add_argument("-z", help='Zoom level, default 2.0', type=float)
    parser.add_argument("-f", help='Desired output image format, default fits',
                        type=str)
    parser.add_argument("-p", help='Pixel in the orginal cutout, default 128',
                        type=int)
    parser.add_argument("--savedir",
                        help='Directory for saving images, default ../HSTImage',
                        type=str)
    parser.add_argument("--catalog",
                        help='Name of the catalog file, default HSTImage.fits',
                        type=str)
    args = parser.parse_args()
    # Set value to corresponding variables
    jsonFile = args.jsonFile
    zoom = setArg(args.z, 2.0)
    formatCode = setArg(args.f, 'fits')
    pixel = setArg(args.p, 128)
    saveDir = setArg(args.savedir, '../HSTImage')
    catalog = setArg(args.catalog, 'HSTImage.fits')
    # Processing json file
    hscData = hscResultParser(hscResultPreparser(jsonFile))
    print("Found " + str(len(hscData)) + " entries")
    # Download images
    make_sure_path_exists(saveDir)
    raList = []
    decList = []
    tnList = []
    for each in hscData:
        try:
            ra = raParser(each[raKeyFinder(each.keys())])
            dec = decParser(each[decKeyFinder(each.keys())])
            imageDownloader(ra, dec, each['ImageName'], each['Target Name'],
                            zoom, formatCode, pixel, saveDir)
            raList.append(ra)
            decList.append(dec)
            tnList.append(each['Target Name'])
        except Exception as reason:
            print(str(ra) + ' ' + str(dec) + ': ' + str(reason) +
                  ' All keys: ' + str(each.keys()))
    # Save a catalog of ra, dec, target name
    c1 = fits.Column(name='ra', array=np.array(raList), format='D')
    c2 = fits.Column(name='dec', array=np.array(decList), format='D')
    c3 = fits.Column(name='targetName', array=tnList, format='50A')
    f = fits.BinTableHDU.from_columns([c1, c2, c3])
    f.writeto(os.path.join(saveDir, catalog), clobber=True)
