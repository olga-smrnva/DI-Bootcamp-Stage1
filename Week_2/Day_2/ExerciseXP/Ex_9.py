# # 1. A movie theater charges different ticket prices depending on a person’s age.
# #	* if a person is under the age of 3, the ticket is free.
# #	* if they are between 3 and 12, the ticket is $10.
# #	* if they are over the age of 12, the ticket is $15

# # 2. Ask a family the age of each person who wants a ticket.
# ages = input('Give me all the ages of of family memebers separated by coma (without space). Press ENTER when you\'re finished \n')

# ages_list = ages.split(',')

# cost = 0

# for age in ages_list :
# 	if int(age) < 3 : cost += 0
# 	elif int(age) < 12 : cost += 10
# 	else : cost += 15


# # 3. Store the total cost of all the family’s tickets and print it out.

# print(cost)

# 4. A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for 
# people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, 
# if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

teenagers = ['John', 'Dan', 'Ammy']
allowed = []

for kid in teenagers : 
	age = int(input(f'How old are you, {kid}?'))
	if age <= 16 or age >= 21 :
		allowed.append(kid)
	else : print(f'Sorry, {kid}, you\'re not allowed')

print(allowed)
