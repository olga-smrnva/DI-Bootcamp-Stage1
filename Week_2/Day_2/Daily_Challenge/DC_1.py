# 1. Ask the user for a number and a length.

number = int(input('Give me a number \n'))
lenght = int(input('Give me a lenght \n'))

# print(number, lenght)

# 2. Create a program that prints a list of multiples of the number until 
#the list length reaches length.

num_list = [number]

for i in range(2, lenght + 1) :
	new_elem = number * i
	num_list.append(new_elem)
	
print(num_list)


