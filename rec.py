import os
import json
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

def readResultCoordinates(imagePath):
    f = open('result/result.json')
    data = json.load(f)
    f.close()
    print(data)

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
