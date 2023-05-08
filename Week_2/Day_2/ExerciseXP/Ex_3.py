basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# 1. Remove “Banana” from the list.
basket.remove('Banana')

# 2. Remove “Blueberries” from the list.
basket.pop()

# 3. Add “Kiwi” to the end of the list.
basket.append('Kiwi')

# 4. Add “Apples” to the beginning of the list.
basket.insert(0, 'Apples')

# 5. Count how many apples are in the basket.

# count = 0
# for fruit in basket : 
# 	if fruit == 'Apples' :
# 		count +=1

count = basket.count('Apples')

# 6. Empty the basket.
basket.clear()

# 7. Print(basket)
print(basket)