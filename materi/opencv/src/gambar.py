import cv2 as cv


class Gambar:
    def __init__(self, show):
        cv.imshow("show", show)
        cv.waitKey(0)