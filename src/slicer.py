import cv2
import numpy
import math
import random

img = cv2.imread("TabelaASCII.png", cv2.IMREAD_GRAYSCALE)
if img is None:
	print("Could not load image");
	exit();

(img_hight,img_width) = img.shape;

slice_hight=86
slice_width=49

ASCII_index = 32
for y in range(0, img_hight, slice_hight):
	for x in range(0,img_width, slice_width):
		new_img = cv2.imread("a.png", cv2.IMREAD_GRAYSCALE);
		for h in range(0,slice_hight):
			for w in range(0,slice_width):
				new_img[h][w] = img[y+h][x+w];
				if(new_img[h][w] > 200):
					print(".", end="")
				else:
					print("0", end="");
			print();

		filename = str(ASCII_index) + ".png"
		print(filename)
		cv2.imwrite(filename, new_img)
		ASCII_index+=1 