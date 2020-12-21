import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w*r), height)
    else:
        r = width / float(w)
        dim = (width, int(h*r))
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized


def show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def edgeDetection(img):
    ratio = img.shape[0] / 500.0
    orig = img.copy()
    image = resize(orig, width=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blur, 75, 200)

    # *************  轮廓检测 ****************
    # 轮廓检测
    contours, hierarchy = cv2.findContours(
        edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

    # 遍历轮廓
    for c in cnts:
        # 计算轮廓近似
        peri = cv2.arcLength(c, True)
        # c表示输入的点集，epsilon表示从原始轮廓到近似轮廓的最大距离，它是一个准确度参数
        approx = cv2.approxPolyDP(c, 0.02*peri, True)

        # 4个点的时候就拿出来
        if len(approx) == 4:
            screenCnt = approx
            break

    # res = cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
    res = cv2.drawContours(image, cnts[0], -1, (0, 255, 0), 2)
    # show(orig)
    show('image', res)


def init():
    image = cv2.imread(args["image"])
    edgeDetection(image)


if __name__ == "__main__":
    init()
