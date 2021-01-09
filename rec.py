import os
import json
import numpy as np
import argparse
import utils.utils as Utils
import pytesseract
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

def getResultList(resultPath, imagePath):
    f = open(resultPath)
    data = json.load(f)
    f.close()
    img = Image.open(imagePath)
    origin_width, origin_height = img.size
    result = Utils.Utils.getAllClassesAndCoordinates(origin_width, origin_height, data)
    return result

def init():
    imagePath = args["image"]
    img = Image.open(imagePath)
    stream = os.popen("./darknet/darknet detector test config/obj.data config/yolov4-tiny-15.cfg config/yolov4-tiny-15_50000.weights -dont_show -ext_output " + imagePath + " -out result/result.json")
    if (stream.read()):
        print('Good!')
        result_list = getResultList('result/result.json', imagePath)
        i = 0
        for item in result_list:
            cropped_image = Utils.Utils.cropImage(img, item['relative_coordinates'][0], item['relative_coordinates'][1], item['relative_coordinates'][2], item['relative_coordinates'][3])
            cropped_image.save("./img" + str(i) + ".jpg")
            i = i + 1
            pass
    else:
        print('Fail')

if __name__ == "__main__":
    init()
