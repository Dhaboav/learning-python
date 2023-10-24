from gambar import *
from video import *


# Membuka gambar
gambar = cv.imread(r"materi\opencv\img.jpeg")
show = Gambar(gambar)

# membuka streaming
streaming = VideoRealTime(0, 320, 320)
streaming.run()

# membuka video
video = Video(r"path/to/video")