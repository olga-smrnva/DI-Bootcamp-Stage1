# 1. Using the list sandwich_orders from the previous exercise, 
# make sure the sandwich ‘pastrami’ appears in the list at least three times.

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
sandwich_orders.extend(['Pastrami sandwich'] * 3)

# print(sandwich_orders)

# 2. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
# and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.

print('The deli has run out of pastrami')
finished_sandwiches = []

while 'Pastrami sandwich' in sandwich_orders:
	sandwich_orders.remove('Pastrami sandwich')
   
for sandwich in sandwich_orders :
	finished_sandwiches.append(sandwich)

# 3. Make sure no pastrami sandwiches end up in finished_sandwiches.

for sandwich in finished_sandwiches :
	print(f'I made you {sandwich}')