# Ask a user for a word

word = input('Give me a word \n')

# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# 	* Make sure the letters are the keys.
# 	* Make sure the letters are strings.
# 	* Make sure the indexes are stored in a list and those lists are values.

word_dictionary = {}

for index in range(len(word)):
	letter = word[index]

	if letter in word_dictionary:
		word_dictionary[letter].append(index)
	else:
		word_dictionary[letter] = [index]

print(word_dictionary)