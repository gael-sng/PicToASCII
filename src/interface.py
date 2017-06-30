
#Initializes
op = 0;
edgechoice = "L8" #Default choice
save = True #Default
printText = False #Default

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
		if save == True:
			# Save text img in a file
			#
		if printText == True:
			# print text img in the terminal
			#
	if op == 2:
		# Set options menu
		print("Choose options:")
		# Set options choices 
		print("\t1- Choose the Edge Detection algorithm.")
		print("\t2- Save resulting text in a file")
		print("\t3- Print resulting text in the terminal")
		op2 = int(input())
		#Set options switch
		if op2 == 1:
			# Choose Edge Menu
			print("Choose Edge Detection:")
			# Choose Edge choices
			print("\t1- Apply Laplacian 4")
			print("\t2- Apply Laplacian 8 (Default)")
			print("\t3- Apply Gaussian and Laplacian 4")
			print("\t4- Apply Gaussian and Laplacian 8")
			op3 = int(input())
			# Choose Edges switch
			if op3 == 1:
				edgechoice = "L4"
			if op3 == 2:
				edgechoice = "L8"
			if op3 == 3:
				edgechoice = "G4"
			if op3 == 4:
				edgechoice = "G8"
		if op2 == 2:
			# Save Text Menu
			print("Save resulting text in a file?")
			# Save Text choices
			print("\t1- Yes (Default)")
			print("\t2- No")
			op3 = int(input())
			# Save Text Switch
			if op3 == 1:
				save = True
			if op3 == 2:
				save = False
		if op2 == 3:
			# Print Text Menu
			print("Printing resulting text in the terminal?")
			# Print Text choices
			print("\t1- Yes")
			print("\t2- No (Default)")
			op3 = int(input())
			# Print Text switch
			if op3 == 1:
				printText = True
			if op3 == 2:
				printText = False
	if op == 3:
		print ("Closing program...")
