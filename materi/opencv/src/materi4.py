import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread(r"materi\opencv\img.jpeg", cv.IMREAD_REDUCED_COLOR_4)
chans = cv.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan, color) in zip(chans, colors):
    hist = cv.calcHist([chan], [0], None, [256], [0,256])
    plt.plot(hist, color = color)
    plt.xlim([0,256])

plt.show()