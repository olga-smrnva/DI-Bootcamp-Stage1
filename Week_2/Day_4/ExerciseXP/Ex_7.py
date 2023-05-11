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