from gambar import *
from video import *


# Membuka gambar
gambar = cv.imread(r"img.jpeg")
show = Gambar(gambar)

# membuka streaming
streaming = VideoRealTime(0, 320, 320)

# membuka video
video = Video(r"path/to/video")