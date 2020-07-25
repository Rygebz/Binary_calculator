while True:
	x = int(input("Enter decimal value: "))
	choice = input("Enter Choice(bin/oct/hex): ")
		
	if choice == 'bin':
		print("Binary value is: \n", bin(x))
		
		break
	elif choice == 'oct':
		print("Octal value is: \n", oct(x))
		
		break	
	elif choice == 'hex':
		print("Hexadecimal value is: \n", hex(x))
		
		break
	else:
		print("Invalid operation")
		
