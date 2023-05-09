# 1. Use the above list called sandwich_orders.
# 2. Make an empty list called finished_sandwiches.

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []


# 3. As each sandwich is made, move it to the list of finished sandwiches.

for sandwich in sandwich_orders :
    finished_sandwiches.append(sandwich)
    
# 4. After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

for sandwich in finished_sandwiches :
    print(f'I made you {sandwich}')