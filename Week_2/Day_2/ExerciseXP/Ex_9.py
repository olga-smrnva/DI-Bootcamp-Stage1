# 1. A movie theater charges different ticket prices depending on a person’s age.
#	* if a person is under the age of 3, the ticket is free.
#	* if they are between 3 and 12, the ticket is $10.
#	* if they are over the age of 12, the ticket is $15

# 2. Ask a family the age of each person who wants a ticket.
ages = input('Give me all the ages of of family memebers separated by coma (without space). Press ENTER when you\'re finished \n')

ages_list = ages.split(',')

cost = 0

for age in ages_list :
    if int(age) < 3 : cost += 0
    elif int(age) < 12 : cost += 10
    else : cost += 15


# 3. Store the total cost of all the family’s tickets and print it out.

print(cost)