import cv2
import numpy as np
from collections import Counter


# Funcao que calcula o valor T para aplicar threshold de uma imagem img
# utiliza-se do metodo de Otsu
def Thresholding_Otsu(img):
  nbins = 256
	pixel_counts  = Counter(img.ravel())
	counts = np.array([0 for x in range(256)])
	for c in sorted(pixel_counts):
		counts[c] = pixel_counts[c]
	p = counts/sum(counts)
	sigma_b = np.zeros((256,1))
	for t in range(nbins):
		q_L = sum(p[:t]) 
		q_H = sum(p[t:]) 
		if q_L ==0 or q_H == 0:
			continue
             
		miu_L = sum(np.dot(p[:t],np.transpose(np.matrix([i for i in range(t)]) )))/q_L
		miu_H = sum(np.dot(p[t:],np.transpose(np.matrix([i for i in range(t,256)]))))/q_H
		sigma_b[t] = q_L*q_H*(miu_L-miu_H)**2
         
	return np.argmax(sigma_b)

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
	w4 = np.array([0, 1, 0, 1, -4, 1, 0, 1, 0])
	w8 = np.array([1, 1, 1, 1, -8, 1, 1, 1, 1])
	# gaussian image
	output_gaussian = cv2.GaussianBlur(img, (7,7), 2)


	if(op == "L4"):
		img = cv2.filter2D(img,-1,w4)
		ret,img = cv2.threshold(imh,Thresholding_Otsu(img),255,cv2.THRESH_BINARY_INV)
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
