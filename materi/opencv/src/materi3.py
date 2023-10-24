from gambar import *
import numpy as np

gambar = cv.imread(r"materi\opencv\img.jpeg")

# ukuran untuk data yang di warp.
width, height = 250,350

# kanan atas, kiri atas, kanan bawah, kiri bawah.
pts1 = np.float32([[926, 302], [523, 148], [691, 847], [319,689]]) 
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# perbaikan sudut pandang
matrix = cv.getPerspectiveTransform(pts1,pts2)
output = cv.warpPerspective(gambar, matrix, (width,height))
show = Gambar(output)