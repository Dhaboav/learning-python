from gambar import *


gambar = cv.imread(r"materi\opencv\img.jpeg")
resize = cv.resize(gambar, (320, 320))
blur = cv.blur(resize, (3,3))
edge = cv.Canny(blur, 25, 100)
contours, _ = cv.findContours(edge, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    cv.drawContours(resize, cnt, -1, (255, 0, 0), 2)

cv.putText(resize, "materi2", (0, 10), cv.FONT_HERSHEY_PLAIN, 
           1.0, (0, 0, 0), 1)
show = Gambar(resize)