# 1. Write a loop that asks a user to enter a series of pizza toppings, 
# when the user inputs ‘quit’ stop asking for toppings.

# 2. As they enter each topping, print a message saying you’ll add that topping to their pizza.

topping = input('What topping do you want to add? (Write \'quit\' when you want to stop) \n')
toppings = []

while topping != 'quit' : 
	print(f'{topping} will be added to your pizza')
	toppings.append(topping)
	topping = input('What topping do you want to add? (Write \'quit\' when you want to stop) \n')

# print(toppings)

# 3. Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

total = 10 + len(toppings) * 2.5

print(f'Total cost will be {total}')
