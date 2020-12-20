import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()


def init():
    print("HIHI")
    image = cv2.imread(args["image"])
    cv_show('image', image)


if __name__ == "__main__":
    init()
