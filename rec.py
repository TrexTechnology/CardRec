import os
import json
import numpy as np
import argparse
import utils.utils as Utils
# import pytesseract
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

def readResultCoordinates(imagePath):
    f = open('result/result.json')
    data = json.load(f)
    print(data)
    img = Image.open(imagePath)
    origin_width, origin_height = img.size
    object1 = data[0]
    x1,x2,y1,y2 = Utils.utils.convergeRelativeCoordinateToAbsoultCoordinates(origin_width, origin_height, object1['objects'][0]['relative_coordinates']['center_x'], object1['objects'][0]['relative_coordinates']['center_y'], object1['objects'][0]['relative_coordinates']['width'], object1['objects'][0]['relative_coordinates']['height'])
    img2 = img.crop((x1,y1,x2,y2))
    img2.save("./img2.jpg")
    f.close()

def init():
    imagePath = args["image"]
    stream = os.popen("./darknet/darknet detector test config/obj.data config/yolov4-tiny-15.cfg config/yolov4-tiny-15_50000.weights -dont_show -ext_output " + imagePath + " -out result/result.json")
    if (stream.read()):
        print('Good!')
        readResultCoordinates(imagePath)
    else:
        print('Fail')

if __name__ == "__main__":
    init()
