import cv2
import numpy
import math
import random
import os

# Pegar inputs: 

img = cv2.imread(os.path.join("Images","cat.jpg"), cv2.IMREAD_GRAYSCALE)
if img is None:
	print("Could not load image");
	exit();

(img_hight,img_width) = img.shape;

print("Image information:")
print("\timg_hight: ", end="");
print(img_hight);
print("\timg_width: ", end="");
print(img_width);
#a =  input();

pixel_multiplayer = 2;

if( pixel_multiplayer < 1 ):
	pixel_multiplayer = 1;

if(pixel_multiplayer > 1):
	# Calculando as novas dimenções
	img_hight = math.floor(img_hight / pixel_multiplayer)
	img_width = math.floor(img_width / pixel_multiplayer)

	new_img = numpy.zeros((img_hight, img_width, 1), numpy.uint8);
	# Reescalando a imagem
	for y in range(0, img_hight):
		for x in range(0, img_width):
			pixel_sum = 0;
			for i in range(0, pixel_multiplayer):
				for j in range(0, pixel_multiplayer):
					pixel_sum += img[(y*pixel_multiplayer)+i][(x*pixel_multiplayer)+j];
			new_img[y][x] = pixel_sum/(pixel_multiplayer * pixel_multiplayer);
					
	print("Image new information:")
	print("\timg_hight: ", end="");
	print(img_hight);
	print("\timg_width: ", end="");
	print(img_width);
	cv2.imwrite("temp.png", new_img)
	img = new_img;
#	a =  input();

# Processamento detectando bordas da imagem deveria acontecer aqui:

# Carregando a lista de caracteres
char = cv2.imread(os.path.join("Font","32.png"), cv2.IMREAD_GRAYSCALE);
if( char is None ):
	print("Could not load image: 32.png");
	exit();
pass

(char_hight,char_width) = char.shape; 

print("Char Image information:")
print("\tchar_hight: ", end="");
print(char_hight);
print("\tchar_width: ", end="");
print(char_width);
#a =  input();

# Arredondando os parametros
img_hight = math.floor(img_hight / char_hight)
img_hight = img_hight * char_hight;
img_width = math.floor(img_width / char_width)
img_width = img_width * char_width;

print("Image new information:")
print("\timg_hight: ", end="");
print(img_hight/char_hight, end="");
print(" caracteres")
print("\timg_width: ", end="");
print(img_width/char_width, end="");
print(" caracteres")

# A imagem grande comaprando os caracteres  
for y in range(0, img_hight, char_hight ):
	for x in range(0, img_width, char_width ):
		# Percorrer todos os caracteres comparando ele com o bloco do caracter
		best_char = 32;
		best_fitness = -1;
		for i in range(0,95):
			dif = 0;
			char = cv2.imread(os.path.join("Font",str(32+i) + ".png"), cv2.IMREAD_GRAYSCALE);
			# Percorrendo o bloco do caracter
			for h in range(0, char_hight):
				for w in range(0, char_width):
					dif += abs(char[h][w] - img[y + h][x + w]);
		
			# Comparando o caracter atual com o melhor até então 
			if( best_fitness > dif or best_fitness == -1 ):
				best_fitness = dif;
				best_char = i + 32;
		# Printando o caracter escolhido
		print(chr(best_char), end="");
		
	print()
