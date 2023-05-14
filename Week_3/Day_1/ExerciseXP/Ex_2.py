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