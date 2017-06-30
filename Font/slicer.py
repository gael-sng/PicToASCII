# Codigo que foi feito apra separar a tabela de imagens dos caracteres
import cv2
import numpy
import math
import random

img = cv2.imread("TabelaASCII_Ulow.png", cv2.IMREAD_GRAYSCALE)
if img is None:
	print("Could not load image");
	exit();

(img_hight,img_width) = img.shape;
print("Image information:")
print("\timg_hight: ", end="");
print(img_hight);
print("\timg_width: ", end="");
print(img_width);
a = input()

slice_hight=21
slice_width=12

ASCII_index = 32
for y in range(0, img_hight, slice_hight):
	for x in range(0,img_width, slice_width):
		new_img = numpy.zeros((slice_hight, slice_width, 1), numpy.uint8);
		for h in range(0,slice_hight):
			for w in range(0,slice_width):
				new_img[h][w] = img[y+h][x+w];
				if(new_img[h][w] > 200):
					print(".", end="")
				else:
					print("0", end="");
			print();

		filename = str(ASCII_index) + "_Ulow.png"
		print(filename)
		cv2.imwrite(filename, new_img)
		ASCII_index+=1 