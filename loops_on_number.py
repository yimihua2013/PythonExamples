
## these are exercises about applying loops on a number in Python###


# is this number a even?
def is_even(x):
	if x % 2==0:
		print (str(x) + " is a even number")
	else:  
		print (str(x) + " isn't a even number")


# function to calculate the factorial of a non-negtive integer
def factorial(y):
	product = 1
	for num in range(y):
		product *= (num+1)
	print ("The factorial of " + str(y) + " is :" + str(product))

# is this a prime number?
def is_prime(z):
	if z > 1:
		for i in range(2,z-1):
			if z % i== 0:
				print ( str(z) + " is not a prime number")
				break
		else:
				print ( str(z) + " is a prime number")
	else:
		print ( str(z) + " is not a prime number")


# execute functions
input = raw_input("Input a number:")
number = int(input)
is_even(number)
is_prime(number)
factorial(number)