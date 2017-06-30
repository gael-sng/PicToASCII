import cv2
import numpy
import math
import random

def modulo (x):
	if x > 0:
		return x;
	else:
		return -x;

img = cv2.imread("cat-2310623_1920.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
	print("Could not load image");
	exit();

# Carregando a lista de caracteres
char = cv2.imread("a.png", cv2.IMREAD_GRAYSCALE);
if char is None:
	print("Could not load char");
	exit();

pixel_multiplayer = 2;
#_fileName = input("Enter the file name: ");
#cv2.imshow("PicToASCII: Input image", img);
#cv2.waitKey(0);
#cv2.destroyAllWindows();

if( pixel_multiplayer < 1 ):
	pixel_multiplayer = 1;

(char_hight,char_width) = char.shape; 

print("Image information:")
print("\tchar_hight: ", end="");
print(char_hight);
print("\tchar_width: ", end="");
print(char_width);
a =  input();

(img_hight,img_width) = img.shape;

print("Image information:")
print("\timg_hight: ", end="");
print(img_hight);
print("\timg_width: ", end="");
print(img_width);
a =  input();

img_hight = math.floor(img_hight / (char_hight * pixel_multiplayer))
img_width = math.floor(img_width / (char_width * pixel_multiplayer))

img_hight = img_hight * (char_hight * pixel_multiplayer)
img_width = img_width * (char_width * pixel_multiplayer)


print("Image new information:")
print("\timg_hight: ", end="");
print(img_hight);
print("\timg_width: ", end="");
print(img_width);
a =  input();

# Percorrendo  
for y in range(0, img_hight, char_hight*pixel_multiplayer ):
	for x in range(0, img_width, char_width*pixel_multiplayer ):
		# Percorrer todos os caracteres comparando ele com o bloco do caracter
		dif = 0;
		# Percorrendo o bloco do caracter
		for h in range(0, char_hight, pixel_multiplayer):
			for w in range(0, char_width, pixel_multiplayer):
				# Percorrer a proporção de pixel na imagem
				resumo_do_pixel = 0;
				for r in range(0, pixel_multiplayer):
					for c in range(0, pixel_multiplayer):
						resumo_do_pixel += img[y+h+r][x+w+c];
				
				resumo_do_pixel = resumo_do_pixel/(pixel_multiplayer * pixel_multiplayer);
				
				dif += modulo(char[h][w] - resumo_do_pixel);
		# Escolher o melhor caracter para colocar neste bloco 
		dif = dif / (pixel_multiplayer*pixel_multiplayer)
		if dif > 5500:
			print("a", end="");
		else:
			print(".", end="");
		
	print()
	WWj
	WWj
	{|}
	|
QWERTYUIOPAS
DFGHJKLÇZXCV
BNM<!?@#$%*)_
{}[]()\|/



