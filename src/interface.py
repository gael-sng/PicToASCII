
#Initializes
op = 0;
edgechoice = "L4" #Default choice

while(op != 3):
	# Main menu
	print("\n\n\n\n")
	print("Image to ascii software.")
	print("Choose an option:")
	# Main menu choices
	print("\t1- Transform image.")
	print("\t2- Set options.")
	print("\t3- Close program.")
	op = int(input())
	# Main menu switch
	if op == 1:
		#Transform image menu
		print("Transform image:")
		print("Give imagem filename.")
		filename = input()
		# Transform code

		
		# end transform code
	if op == 2:
		# Set options menu
		print("Choose options:")
		# Set options choices
		print("\t1- Choose the Edge Detection algorithm.")
		op2 = int(input())
		#Set options switch
		if op2 == 1:
			# Choose Edge Menu
			print("Choose Edge Detection:")
			# Choose Edge choices
			print("\t1- Apply Laplacian 4 (Default)")
			print("\t2- Apply Laplacian 8")
			print("\t3- Apply Gaussian and Laplacian 4")
			print("\t4- Apply Gaussian and Laplacian 8")
			op3 = input()
			# Choose Edges switch
			if op3 == 1:
				edgechoice = "L4"
			if op3 == 2:
				edgechoice = "L8"
			if op3 == 3:
				edgechoice = "G4"
			if op3 == 4:
				edgechoice = "G8"
	if op == 3:
		print ("Closing program...")
