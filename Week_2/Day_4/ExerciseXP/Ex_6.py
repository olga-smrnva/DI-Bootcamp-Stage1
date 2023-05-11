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