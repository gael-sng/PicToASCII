from PicToASCII import PicToASCII

#Initializes
op = 0;
edgechoice = "L8" #Default choice
save = True #Default
printText = False #Default
char_quality = "_Ulow.png"
pixel_reason = 1;
image_Name = "frog.png"

while(op != 3):
	print("Press Enter")
	input()
	# Main menu
	print("\n\n\n\n\n\n\n\n\n\n\n\n")
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
		print("Give image filename.(Default = ENTER)")
		filename = input()
		if(filename == "\n" or filename == "" or filename is None):
			print("frog selected")
		else:
			image_Name = filename
		# Transform code
		ASCII_Art = PicToASCII(char_quality,pixel_reason,edgechoice,image_Name)
		if ASCII_Art is not None:
			# end transform code
			if save == True:
				# Save text img in a file
				print("Saving File")
				file = open("Output.txt", "w")
				file.write(ASCII_Art);

			if printText == True:
				# print text img in the terminal
				print("Printing Text:")
				print(ASCII_Art)
	if op == 2:
		# Set options menu
		print("Choose options:")
		# Set options choices 
		print("\t1- Choose the Edge Detection algorithm.")
		print("\t2- Save resulting text in a file")
		print("\t3- Print resulting text in the terminal")
		print("\t4- Change char quality")
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
		if op2 == 4:
			#char quality
			print("Choose char quality:")
			print("\t1- Ultra Low")
			print("\t2- Low")
			print("\t3- High")
			op3 = int(input())
			# Char quality switch
			if op3 == 1:
				char_quality = ".png"
			if op3 == 2:
				char_quality = "_low.png"
			if op3 == 3:
				char_quality = "_Ulow.png"
	if op == 3:
		print ("Closing program...")
