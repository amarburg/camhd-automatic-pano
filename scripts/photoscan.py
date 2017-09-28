#!/usr/bin/env python3

import logging
import PhotoScan
import glob
import os

import argparse


parser = argparse.ArgumentParser(description='Generate HTML proofs')

# parser.add_argument('input', nargs='?',
#                     help='Regions files to process',
#                     default=False)
#
# parser.add_argument('--force', dest='force', action='store_true', help='Force re-download of images')

# parser.add_argument('--squash-runs', dest='squashruns', action='store_true', help='Squash runs of multiple identical tags')

parser.add_argument('--log', metavar='log', nargs='?', default='INFO',
                    help='Logging level')

parser.add_argument('--input', nargs='?', default='images/', help='Working directory')
#
# parser.add_argument('--image-size', dest='imgsize', nargs='?', default='320x240')

# parser.add_argument('--with-groundtruth', dest='groundtruth', action='store_true')
#
# parser.add_argument("--ground-truth", dest="groundtruthfile",
#                     default="classification/ground_truth.json")
#
# parser.add_argument("--image-format", dest="imageext", default='jpg')
#
# parser.add_argument('--lazycache-url', dest='lazycache', default=os.environ.get("LAZYCACHE_URL", None),
#                     help='URL to Lazycache repo server (only needed if classifying)')

args = parser.parse_args()
logging.basicConfig( level=args.log.upper() )

logging.info("Photoscan %s activated" % ("is" if PhotoScan.Application.activated else "is not"))

doc = PhotoScan.app.document
chunk = doc.addChunk()
group = chunk.addCameraGroup()
group.type = PhotoScan.CameraGroup.Station

images = glob.glob( args.input + "/*")

if len(images) == 0:
    logging.warning("Found no images in %s" % args.input)
    exit(-1)

logging.info("Adding %d images" % len(images))

chunk.addPhotos( images, PhotoScan.FlatLayout )

for c in chunk.cameras:
    c.group = group

chunk.matchPhotos(accuracy=PhotoScan.HighAccuracy, generic_preselection=True, reference_preselection=False)
chunk.alignCameras()

chunk.buildDenseCloud(quality=PhotoScan.MediumQuality)

chunk.buildModel(surface=PhotoScan.Arbitrary, interpolation=PhotoScan.EnabledInterpolation)

doc.save(path="%s/project.psx" % os.getcwd(), chunks=doc.chunks)
