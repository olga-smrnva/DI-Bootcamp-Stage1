#___________________________________
# 1

class Cat:
	def __init__(self, cat_name, cat_age):
		self.name = cat_name
		self.age = cat_age

# 1. Instantiate three Cat objects using the code provided above.

cat1 = Cat('Sussy', 3)
cat2 = Cat('Murmur', 7)
cat3 = Cat('Puss', 4)

# 2. Outside of the class, create a function that finds the oldest cat and returns the cat.

def get_oldest_cat(cat1, cat2, cat3):
	oldest = max(cat1.age, cat2.age, cat3.age)
	if oldest ==  cat1.age : return (f"The oldest cat is {cat1.name} {cat1.age} years old.")
	elif oldest == cat2.age : return (f"The oldest cat is {cat2.name} {cat2.age} years old.")
	elif oldest == cat3.age : return (f"The oldest cat is {cat3.name} {cat3.age} years old.")

# 3. Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

print(get_oldest_cat(cat1, cat2, cat3))

#___________________________________
# 2

# 1. Create a class called Dog.
# 2. In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.

class Dog:
	def __init__(self, dog_name, dog_height):
		self.name = dog_name
		self.height = dog_height

	# 3. Create a method called bark that prints the following string “<dog_name> goes woof!”.

	def bark(self):
		print(f"{self.name} goes woof!")

	# 4. Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.

	def jump(self):
		print(f'{self.name} jumps {self.height * 2} cm high!')

# 5. Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.

davids_dog = Dog('Rex', 50)

# 6. Print the details of his dog (ie. name and height) and call the methods bark and jump.

print(f'The dog\'s name is {davids_dog.name} and it\'s height is {davids_dog.height}')
davids_dog.bark()
davids_dog.jump()

# 7. Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.

sarahs_dog = Dog('Teacup', 20)

# 8. Print the details of her dog (ie. name and height) and call the methods bark and jump.

print(f'The dog\'s name is {sarahs_dog.name} and it\'s height is {sarahs_dog.height}')
sarahs_dog.bark()
sarahs_dog.jump()

# 9. Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

if sarahs_dog.height > davids_dog.height: print(f'Sarah\'s dog is bigger')
elif sarahs_dog.height < davids_dog.height: print(f'David\'s dog is bigger')
else : print ('Dogs are of the same height')

#___________________________________
# 3

# 1. Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).

class Song:
	def __init__(self, song_lyrics):
		self.lyrics = song_lyrics

# 2. Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.

	def sing_me_a_song (self):
		print(*self.lyrics, sep='\n')
		

# 3. Create an object, for example:

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# 4. Then, call the sing_me_a_song method.

stairway.sing_me_a_song()

#___________________________________
# 4

