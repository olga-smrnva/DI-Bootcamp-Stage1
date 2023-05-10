# 1. Write a function called describe_city() that accepts the name of a city and its country as parameters.

# 2. The function should print a simple sentence, such as "<city> is in <country>".
# 	For example “Reykjavik is in Iceland”

# 3. Give the country parameter a default value.

def describe_city(city, country = 'Israel') :
    print(f'{city} is in {country}')


# 4. Call your function.

describe_city('Tel Aviv')