# 1

# 1. Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.

def display_message() :
    print('Hey there, I\'m stuidying Python!')

# 2. Call the function, and make sure the message displays correctly.

display_message()

#___________________________________
# 2

# 1. Write a function called favorite_book() that accepts one parameter called title.

# 2. The function should print a message, such as "One of my favorite books is <title>". For example: “One of my favorite books is Alice in Wonderland”

def favorite_book(title) :
    print(f'One of my favorite books is {title}')

# 3. Call the function, make sure to include a book title as an argument when calling the function.

favorite_book('Harry Potter')

#___________________________________
# 3

# 1. Write a function called describe_city() that accepts the name of a city and its country as parameters.

# 2. The function should print a simple sentence, such as "<city> is in <country>".
# 	For example “Reykjavik is in Iceland”

# 3. Give the country parameter a default value.

def describe_city(city, country = 'Israel') :
    print(f'{city} is in {country}')


# 4. Call your function.

describe_city('Tel Aviv')


#___________________________________
# 4

# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
import random

def compare_numbers(num) :
    num = int(num)
    if num < 1 or num > 100 : return False
    
    second_num = random.randint(1,100)
    if num == second_num :
        print(f'Success, numbers are the same: {num, second_num}')
    else : print(f'Failure, numbers are different: {num, second_num}')
    
    
compare_numbers(44)

#___________________________________
# 5

# 1. Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.

# 2. The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"

def make_shirt(size, text) :
	print(f'The size of the shirt is {size} and the text is {text}')

# 3. Call the function make_shirt().

make_shirt('M', 'Hellloooo')

# 4. Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.

def make_shirt(size='L', text='I love Python'):
	print(f'The size of the shirt is {size} and the text is {text}')

# 5. Make a large shirt with the default message

make_shirt()

# 6. Make medium shirt with the default message

make_shirt('M')

# 7. Make a shirt of any size with a different message.

make_shirt('M', 'Beauty')

#___________________________________
# 6

# 1. Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# 2. Pass the list to a function called show_magicians(), which prints the name of each magician in the list.

def show_magicians(magicians) :
	for magician in magicians :
		print(magician)

show_magicians(magician_names)

# 3. Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.

def make_great(magicians) :
	magicians = ['The Great ' + magician for magician in magicians]
	return magicians

# 4. Call the function make_great().
# 5. Call the function show_magicians() to see that the list has actually been modified.

magician_names = make_great(magician_names)
show_magicians(magician_names)

#___________________________________
# 7

