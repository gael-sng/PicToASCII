# Image genarator assignment
# Gabriel Simmel Nascimento Nºusp:9050232
import cv2
import numpy
import math
import random

def f1 (a,b,c):
	return a+b;

# Taking the data from keyboard 
img = cv2.imread("cameraman.png", cv2.IMREAD_GRAYSCALE)
char = cv2.imread("a.png", cv2.IMREAD_GRAYSCALE)
if img is None:
	print("Could not load image")
#_fileName = input("Enter the file name: ");

#cv2.imshow("PicToASCII: Input image", img);
#cv2.waitKey(0);
#cv2.destroyAllWindows();

(char_hight,char_width) = char.shape 

for h in range(0, char_hight):
	for w in range(0, char_width):
		if char[h][w] < 200 :
			print("0", end="");
		else:
			print(".", end="");
	print();

(img_hight,img_width) = img.shape 

for y in range(0, img_hight, char_hight):
	for x in range(0, img_width, char_width):
		dif = 0;
		# Percorrendo o bloco do caracter
		for h in range(0, char_hight):
			for w in range(0, char_width):
				if y+h < img_hight and x+w < img_width:
					dif += img[y+h][x+w] - char[h][w]
		if dif < 13000:
			print("0", end="")
		else:
			print(".", end="")
	print()

# Saving resulted image in a file
#cv2.imwrite(_fileName,img);
