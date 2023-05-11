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