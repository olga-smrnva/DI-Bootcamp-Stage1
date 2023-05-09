# 1. A movie theater charges different ticket prices depending on a person’s age.
#	* if a person is under the age of 3, the ticket is free.
#	* if they are between 3 and 12, the ticket is $10.
#	* if they are over the age of 12, the ticket is $15.

# 2. Given the following object:

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# 3. How much does each family member have to pay?

cost = 0

for member in family :
    if family[member] < 3 : cost += 0
    elif family[member] < 12 : cost += 10
    else : cost += 15
     

# 4. Print out the family’s total cost for the movies.

print(f'The total cost for the whole family will be: {cost}')


# 5. Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

new_family = {}
member_name = input('Hello, do you want to enter your family\'s info? \n(YES\QUIT) ')

while member_name != 'QUIT' :
    member_name = input("Enter family member's name: ") 
    if member_name == 'QUIT' :
        break 
    member_age = int(input("Enter family member's age: "))
    # member_age = int(member_age)

    new_family[member_name] = member_age

print(new_family)