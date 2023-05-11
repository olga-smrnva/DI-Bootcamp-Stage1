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

# 1. Create a function called get_random_temp().
# 	* This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
#  	* Test your function to make sure it generates expected results.

import random

def get_random_temp() :
	return random.randint(-10, 40) 

# print(get_random_temp())

# 2. Create a function called main().
#  	* Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
#  	* Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

def main() :
	temp = get_random_temp()
	print(f'The temperature right now is {temp} degrees Celsius')
	
main()

# 3. Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
#  	* below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
#  	* between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
#  	* between 16 and 23
#  	* between 24 and 32
#  	* between 32 and 40

def main() :
	temp = get_random_temp()
	if temp < 0 : print('Brrr, that\'s freezing! Wear some extra layers today')
	elif temp >= 0 and temp < 16 : print('Quite chilly! Don\'t forget your coat')
	elif temp >= 16 and temp < 32 : print('It\'s quite pleasant outside. Go for a walk')
	else : print('OMG, stay at home under the mazgan')
	
main()

# 4. Change the get_random_temp() function:
#   * Add a parameter to the function, named season’.
#  	* Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is winter’, temperatures should only fall between -10 and 16.
#  	* Now that we’ve changed get_random_temp(), let’s change the main() function:
#  		* Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
#  		* Use the season as an argument when calling get_random_temp().

def get_random_temp(season) :
    season_temp = {
        'winter': [-10, 16],
        'spring': [10, 25],
        'summer': [18, 40],
        'autumn': [-2, 22]
    }
    return random.randint(*season_temp[season])
    
def main() :
	season = input('Give me one season typing summer, autumn, winter, or spring: \n')
	temp = get_random_temp(season)
	if temp < 0 : print('Brrr, that\'s freezing! Wear some extra layers today')
	elif temp >= 0 and temp < 16 : print('Quite chilly! Don\'t forget your coat')
	elif temp >= 16 and temp < 32 : print('It\'s quite pleasant outside. Go for a walk')
	else : print('OMG, stay at home under the mazgan')

main()