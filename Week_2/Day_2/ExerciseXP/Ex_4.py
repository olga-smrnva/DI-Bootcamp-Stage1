# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 
# (don’t hard-code the sequence)

my_list = []
element = 1.5

while element <= 5 :
	my_list.append(element)
	element += 0.5
	
	if element%int(element) == 0 :
		element = int(element)

print(my_list)	
