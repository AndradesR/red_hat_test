# This is a very simple Python app that will check 100 numbers and validate if the remainder of their divisions per 2, 5 or both 
# will return 0. This would validate if they are multiples of those numbers

if __name__ == '__main__':
 
	for number in range(1,101): 
		if (number % 2 == 0) & (number % 5 == 0): # verifies if the variable 'number' is multiple of 2 and 5 using the modulus operator
			print "Redhat" + " = " + str(number) 
		elif (number % 2 == 0): # verifies if 'number' is multiple of 2 using the same operator
			print "red" + " = " + str(number) 
		elif (number % 5 == 0): # verifies if 'number' is multiple of 5 using the same operator
			print "hat" + " = " + str(number) 


    	