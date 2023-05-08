# 1. Use a for loop to print all numbers from 1 to 20, inclusive.
numbers = range(1, 21)

# for number in numbers : 
	# print(number)

# 2. Using a for loop, that loops from 1 to 20(inclusive), 
# print out every element which has an even index.

for number in numbers :
	if numbers.index(number)%2 == 0 :
		print(number)
