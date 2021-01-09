import os
import platform
import json
import argparse
import utils.utils as Utils
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
    result = Utils.Utils.getAllClassesAndCoordinates(
        origin_width, origin_height, data)
    return result


def init():
    imagePath = args["image"]
    image = Image.open(imagePath)
    if (platform.system() == 'Windows'):
        stream = os.popen(".\darknet\darknet detector test config/obj.data config/yolov4-tiny-15.cfg config/yolov4-tiny-15_50000.weights -dont_show -ext_output " +
                          imagePath + " -out result/result.json")
    else:
        stream = os.popen("./darknet/darknet detector test config/obj.data config/yolov4-tiny-15.cfg config/yolov4-tiny-15_50000.weights -dont_show -ext_output " +
                          imagePath + " -out result/result.json")
    if (stream.read()):
        result_list = getResultList('result/result.json', imagePath)
        result_list = Utils.Utils.integrateOCRResult(image, result_list)
        print(result_list)
    else:
        print('Fail')


if __name__ == "__main__":
    init()
