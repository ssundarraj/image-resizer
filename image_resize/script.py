import os
import sys
from PIL import Image
import argparse


def console_main():
    parser = argparse.ArgumentParser(
                description='Downloads images from given URL')
    parser.add_argument('img2resize', nargs='*', help="Image to resize")
    parser.add_argument('-s', '--size', type=int, nargs=2, default=[1024, 1024],
                        help="Size of the image output. <height>, <width>")
    parser.add_argument('-a', '--appstring', type=str, default="_thumbnail",
                        help="String to be appended to the file output.")
    args = parser.parse_args()
    size = tuple(args.size)
    appstring = args.appstring
    img2resize = args.img2resize
    for infile in img2resize:
        outfile = os.path.splitext(infile)[0] + appstring + ".jpg"
        if infile != outfile:
            try:
                im = Image.open(infile)
                im.thumbnail(size, Image.ANTIALIAS)
                im.save(outfile, "JPEG")
                print "Resied '{0}' to '{1}'.".format(infile, outfile)
            except IOError:
                print "cannot create thumbnail for '{0}'.".format(infile)
