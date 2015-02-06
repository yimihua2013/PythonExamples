# more loop excersices

'''define a function to return the number of times the item occurs in the list.
For example: 
count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list)
'''
def count(sequence, item):
	item_count=0
	for i in range(len(sequence)):
		if sequence[i]==item:
			item_count+=1
	return item_count
     

'''
Define a function called purify that takes in a list of numbers, 
removes all odd numbers in the list, and returns the result.
'''
def purify(seq):
	even_list=[]
	for i in range(len(seq)):
		if seq[i]%2==0:
			even_list.append(seq[i])
	return even_list


'''
Define a function called product that takes a list of integers as input and 
returns the product of all of the elements in the list.
For example: 
product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100)
'''
def product(seqs):
	result= 1
	for i in range(len(seqs)):
		result *= seqs[i]
	return result


# execute the functions

num_list = [2,4,5,78,9,10,4]
print "the even numbers are: " + str(purify(num_list))
print "4 appears " + str(count(num_list, 4)) + " times" + " in the list" +" "+ str(num_list)
print "The product of the list " +str(num_list)+ " is: " + str(product(num_list))


