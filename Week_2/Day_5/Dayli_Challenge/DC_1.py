# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

inp_string = input('Give me a comma separated sequence of words: \n')
inp_list = inp_string.split(',')
inp_list.sort()

# Use List Comprehension
print(*(word for word in inp_list))




