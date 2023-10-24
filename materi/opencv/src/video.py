import cv2 as cv

class VideoRealTime:
    def __init__(self, indeks, height, width):
        self.indeks = indeks
        self.height = height
        self.width = width

    def run(self):
        camera = cv.VideoCapture(self.indeks, cv.CAP_DSHOW)
        camera.set(cv.CAP_PROP_FRAME_HEIGHT, self.height)
        camera.set(cv.CAP_PROP_FRAME_WIDTH, self.width)
        while camera.isOpened():
            ret, frame = camera.read()
            cv.imshow("Video", frame)
            if cv.waitKey(24) & 0xFF == ord("x"):
                break

        camera.release()
        cv.destroyWindow("Video")


class Video:
    def __init__(self, path):
        camera = cv.VideoCapture(path)
        while camera.isOpened():
            ret, frame = camera.read()
            cv.imshow("Video", frame)
            if cv.waitKey(24) & 0xFF == ord("x"):
                break

        camera.release()
        cv.destroyWindow("Video")