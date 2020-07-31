op = 1
chr(op)

while(op != 'e'):
	choice = input("Enter Choice(bin/oct/hex): ")
	x = int(input("Enter decimal value: "))
		
	if choice == 'bin':
		print("Binary value is: \n", bin(x))
		print("Are u want to continue, y or n?")
		choice = input("Enter opertation: ")
		while True:
			if choice == 'y': 
				x = int(input("Enter decimal value: "))
				print("Binary value is: \n", bin(x))	
				print("Are u want to continue, y or n?")
				choice = input("Enter opertation: ")
			break	
		if choice == 'n':
			print(" Enter Choice(bin/oct/hex)")
			choice = input("Enter operation: ")
	elif choice == 'oct':
		print("Octal value is: \n", oct(x))
		print("Are u want to continue, y or n?")
		choice = input("Enter opertation: ")
		while True:
			if choice == 'y':
				x = int(input("Enter decimal value: "))
				print("Octal value is: \n", oct(x))
				print("Are u want to continue, y or n ?")
				choice = input("Enter opertation: ")
			break	
		if choice == 'n':
			print(" Enter Choice(bin/oct/hex)")
			choice = input("Enter operation: ")
	elif choice == 'hex':
		print("Hexadecimal value is: \n", hex(x))
		print("Are u want to continue, y or n?")
		choice = input("Enter opertation: ")
		while True:
			if choice == 'y': 
				x = int(input("Enter decimal value: "))
				print("Hexadecimal value is: \n", hex(x))
				print("Are u want to continue, Y or N ?")
				choice = input("Enter opertation: ")
			break	
		if choice == 'n':
			print(" Enter Choice(bin/oct/hex)")
			choice = input("Enter operation: ")
	else:
		print("Invalid operation")
