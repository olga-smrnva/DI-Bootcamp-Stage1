# Write a program that asks a string to the user, and display 
#a new string with any duplicate consecutive letters removed.

my_string = input('Please, write something \n')

new_string = ''

for character in my_string :
    if new_string == '' or character != new_string[len(new_string) - 1] : 
            new_string = new_string + character
                
print(new_string)