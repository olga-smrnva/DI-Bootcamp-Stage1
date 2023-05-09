brand = {
	'name': 'Zara',
	'creation_date': 1975 ,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue', 
        'Spain': 'red',
        'US': ['pink', 'green']
	}
}

#  Change the number of stores to 2.
brand['number_stores'] = 2

#  Print a sentence that explains who Zaras clients are.
clients = ''
brand['type_of_clothes'].pop()
for client in brand:
    clients = ', '.join(brand['type_of_clothes'])

print(f'Zara\'s clients usually are: {clients}')

# Add a key called country_creation with a value of Spain.

brand['country_creation'] = 'Spain'

#Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.

if brand['international_competitors'] :
    brand['international_competitors'].append('Desigual')

#Delete the information about the date of creation.

del brand['creation_date']

#  Print the last international competitor.

print(brand['international_competitors'][len(brand['international_competitors']) - 1])

# Print the major clothes colors in the US.

major_colors = ', '.join(brand['major_color']['US'])
print(f'Major clothes colors in the US are: {major_colors}')

# Print the amount of key value pairs (ie. length of the dictionary).

print(f'The amount of keys is equal to {len(brand)}')

# Print the keys of the dictionary.

keys = ''
for key in brand :
    keys = ', '.join(brand.keys())
    
print(f'All the keys are: {keys}')

# Create another dictionary called more_on_zara with the following details:
# creation_date: 1975 
# number_stores: 10 000

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}


# Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)

# Print the value of the key number_stores. What just happened ? 

print(brand['number_stores'])