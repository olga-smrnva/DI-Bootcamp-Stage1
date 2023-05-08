# 1. Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
fruits = input('What are you favourite fruits? Type and separate the fruits with a single space \n')

# 2. Store the favorite fruit(s) in a list (convert the string of words into a list of words).
list_fruits = fruits.split()

# print(list_fruits)

# 3. Now that we have a list of fruits, ask the user to input a name of any fruit.
#   *If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
#   *If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

new_fruit = input('Give me one more fruit \n')
isFruit = False
for fruit in list_fruits :
    if fruit == new_fruit :
        isFruit = True	   

if isFruit == True :
    print('You chose one of your favorite fruits! Enjoy!')
else : print('You chose a new fruit. I hope you enjoy')
    
