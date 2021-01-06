import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())


def init():
    image = cv2.imread(args["image"])

if __name__ == "__main__":
    init()
