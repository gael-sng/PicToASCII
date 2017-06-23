# Image genarator assignment
# Gabriel Simmel Nascimento Nºusp:9050232
import cv2
import numpy
import math
import random

def f1 (a,b,c):
		return a+b;

def f2 (a,b,c):
		res = math.sin(a/c) * 255;
		if res > 0 :
			return res;
		else :
			return -res;

def f3 (a,b,c):
		return ((a/c)*(a/c) + 2*(b/c)*(b/c)) * 255;

def f4 (a,b,c):
		return random.random()*255;

print("\nImage genarator version 1.0\nGabriel Simmel Nascimento N.usp:9050232\n");


# Taking the data from keyboard 
_fileName = input("Enter the file name: ");
str = input("Enter the lateral size: ");
_lateral_size = eval(str);

print("Avaible functions:");
print("\t1. f(x, y) = (x + y)");
print("\t2. f(x, y) = |sin(x/Q) x 255|");
print("\t3. f(x, y) = [(x/Q)^2 + 2(y/Q)^] x 255");
print("\t4. f(x, y) = rand(0, 255)\n");

# Loop that will ask for a answer until the user give a valid answer
_function = input("Enter the function number: ");
while _function != '1' and _function != '2' and _function != '3' and _function != '4' :
	_function = input("Enter the function number: ");

Q = float(input("Enter a frequency parameter: "));


# Creating de empty grayscale image ith the especific size
img = numpy.zeros((_lateral_size, _lateral_size, 1), numpy.uint8);

# Assigning the chosen function to the function pointer
chosenFunc = f1;
if _function == '1':
	chosenFunc = f1;

elif _function == '2':
	chosenFunc = f2;

elif _function == '3':
	chosenFunc = f3;

elif _function == '4':
	chosenFunc = f4;

# Generating the image based on the chosen function
for x in range(_lateral_size):
	for y in range(_lateral_size):
		img[x][y] = chosenFunc(x,y,Q) % 255;

# Showing the results
#cv2.imshow("Result",img);
#cv2.waitKey(0);
#cv2.destroyAllWindows();

# Saving resulted image in a file
cv2.imwrite(_fileName,img);
