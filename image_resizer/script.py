import os, sys
from PIL import Image
import argparse


def console_main():
    parser = argparse.ArgumentParser(
                description='Downloads images from given URL')
    parser.add_argument('img2resize', nargs=1, help="Image to resize")
    parser.add_argument('-s', '--size', type=int, nargs=2, default="1024, 1024",
                help="Size of the image output. <height>, <width>")
    args = parser.parse_args()
    size = tuple(args.size)
    img2resize=args.img2resize
    for infile in img2resize:
        outfile = os.path.splitext(infile)[0] + "_thumbnail.jpg"
        if infile != outfile:
            try:
                im = Image.open(infile)
                im.thumbnail(size, Image.ANTIALIAS)
                im.save(outfile, "JPEG")
            except IOError:
                print "cannot create thumbnail for '%s'" % infile
