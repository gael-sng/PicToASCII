import cv2
import numpy
import math
import random
import os
#import Edgedetection

import numpy as numpy
from collections import Counter



# Funcao que calcula o valor T para aplicar threshold de uma imagem img
# utiliza-se do metodo de Otsu
def Thresholding_Otsu(img):
	nbins = 256
	pixel_counts  = Counter(img.ravel())
	counts = numpy.array([0 for x in range(256)])
	for c in sorted(pixel_counts):
		counts[c] = pixel_counts[c]
	p = counts/sum(counts)
	sigma_b = numpy.zeros((256,1))
	for t in range(nbins):
		q_L = sum(p[:t]) 
		q_H = sum(p[t:]) 
		if q_L ==0 or q_H == 0:
			continue
             
		miu_L = sum(numpy.dot(p[:t],numpy.transpose(numpy.matrix([i for i in range(t)]) )))/q_L
		miu_H = sum(numpy.dot(p[t:],numpy.transpose(numpy.matrix([i for i in range(t,256)]))))/q_H
		sigma_b[t] = q_L*q_H*(miu_L-miu_H)**2
         
	return numpy.argmax(sigma_b)

#Essa funcao pega uma imagem e realiza um dos 4 metodos de edge detection
# 1-L4- Aplica apenas o Laplacian filter 4 [0, 1, 0, 1, -4, 1, 0, 1, 0]
# 2-L8- Aplica apenas o Laplacian filter 8 [1, 1, 1, 1, -8, 1, 1, 1, 1]
# 3-G4- Aplica Gaussian filter e depois Laplacian 4
# 4-G8- Aplica Gaussian filter e depois Laplacian 8
# Todos os metodos no final passam por um Threshold com T sendo obtido atraves do metodo Otsu
# Com a definicao cv2.THRESH_BINARY_INV, a imagem ficara com o fundo branco e as bordas pretas

def Edgedetection(imgaux,op):

	img = imgaux.copy()
	# Laplacian Filter
	w4 = numpy.array([0, 1, 0, 1, -4, 1, 0, 1, 0])
	w8 = numpy.array([1, 1, 1, 1, -8, 1, 1, 1, 1])
	# gaussian image
	output_gaussian = cv2.GaussianBlur(img, (7,7), 2)


	if(op == "L4"):
		img = cv2.filter2D(img,-1,w4)
		ret,img = cv2.threshold(img,Thresholding_Otsu(img),255,cv2.THRESH_BINARY_INV)
	if(op == "L8"):
		img = cv2.filter2D(img,-1,w8)
		ret,img = cv2.threshold(img,Thresholding_Otsu(img),255,cv2.THRESH_BINARY_INV)
	if(op == "G4"):
		img = cv2.filter2D(output_gaussian,-1,w4)
		ret,img = cv2.threshold(img,Thresholding_Otsu(img),255,cv2.THRESH_BINARY_INV)
	if(op == "G8"):
		img = cv2.filter2D(output_gaussian,-1,w8)
		ret,img = cv2.threshold(img,Thresholding_Otsu(img),255,cv2.THRESH_BINARY_INV)

	return img

def Rescale(imgaux, pixel_reason):

	(imgaux_hight,img_width) = imgaux.shape;
	# Calculando as novas dimenções
	imgaux_hight = math.floor(imgaux_hight / pixel_reason)
	img_width = math.floor(img_width / pixel_reason)

	new_img = numpy.zeros((imgaux_hight, img_width, 1), numpy.uint8);
	# Reescalando a imagem
	for y in range(0, imgaux_hight):
		for x in range(0, img_width):
			pixel_sum = 0;
			for i in range(0, pixel_reason):
				for j in range(0, pixel_reason):
					pixel_sum += imgaux[(y*pixel_reason)+i][(x*pixel_reason)+j];
			new_img[y][x] = pixel_sum/(pixel_reason * pixel_reason);
				
	
	cv2.imwrite("rescale.png", new_img)
	return new_img

#====================================
#=== MAIN CODE ======================
#====================================
def PicToASCII(char_quality,pixel_reason,edge_function,image_Name):
	# Pegar inputs:
	img = cv2.imread(os.path.join("Images",image_Name), cv2.IMREAD_GRAYSCALE)
	if img is None:
		print("Could not load image");
		return None

	if(pixel_reason > 1):
		img = Rescale(img, pixel_reason)

	# Processamento detectando bordas da imagem deveria acontecer aqui:
	if (edge_function != "none"):
		img = Edgedetection(img, edge_function)
		cv2.imwrite("edge.png", img)

	# Carregando a lista de caracteres
	char = cv2.imread(os.path.join("Font","32" + char_quality), cv2.IMREAD_GRAYSCALE);
	if( char is None ):
		print("Could not load image: 32" + char_quality);
		return None

	(img_hight, img_width) = img.shape;

	(char_hight, char_width) = char.shape; 

	# Arredondando os parametros
	img_hight = math.floor(img_hight / char_hight)
	img_hight = img_hight * char_hight;
	img_width = math.floor(img_width / char_width)
	img_width = img_width * char_width;

	ASCII_Art = ""

	# A imagem grande comaprando os caracteres  
	for y in range(0, img_hight, char_hight ):
		for x in range(0, img_width, char_width ):
			# Percorrer todos os caracteres comparando ele com o bloco do caracter
			best_char = 32;
			best_fitness = -1;
			for i in range(0,95):
				dif = 0;
				char = cv2.imread(os.path.join("Font",str(32+i) + char_quality), cv2.IMREAD_GRAYSCALE);
				# Percorrendo o bloco do caracter
				for h in range(0, char_hight):
					for w in range(0, char_width):
						dif += abs(char[h][w] - img[y + h][x + w]);
			
				# Comparando o caracter atual com o melhor até então 
				if( best_fitness > dif or best_fitness == -1 ):
					best_fitness = dif;
					best_char = i + 32;
			# Printando o caracter escolhido
			#print(chr(best_char), end="");
			ASCII_Art += chr(best_char)
			
		#print()
		ASCII_Art+= '\n'
	return ASCII_Art
