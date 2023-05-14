# 1. Create a class called Zoo.

# 2. In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).

class Zoo:
	def __init__(self, zoo_name):
		self.animals = []
		self.name = zoo_name

# 3. Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.

	def add_animal(self, new_animal): 
		for animal in self.animals:
			if new_animal != animal:
				self.animals.append(new_animal) 
		


# 4. Create a method called get_animals that prints all the animals of the zoo.

	def get_animals(self):
		print(*(self.animals), spl=', ')



# 5. Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.

	def sell_animal(self, animal_sold):
		sold_animals = []
		for animal in self.animals:
			if animal_sold == animal:
				sold_animals.append(animal_sold)
				self.animals.remove(animal_sold)


# 6. Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.

	# def sort_animals(self):
	# 	self.animals.sort()
	# 	sorted_animals = {}
	# 	key = 1
	# 	for animal in self.animals:
	# 		if animal[0] != animal[0]:
	# 			sorted_animals[key] = animal
	# 			key += 1
	# 		else : pass


# 7. Create a method called get_groups that prints the animal/animals inside each group.

	# def get_groups(self):
	# 	print('Groups:')
		
	# 	for k, v in self.sorted_animals.items():
	# 		print (f'{k}: {v}')
		
	# 	print(self.__dict__)

# 8. Create an object called ramat_gan_safari and call all the methods.

ramat_gan_safari = Zoo('Ramat Gan Safari')

while True:
    new_animal = input('Which animal do you want to see in our zoo? Type here (print "quit" to stop): \n')
    if new_animal == 'quit': break
    ramat_gan_safari.add_animal(new_animal)
    ramat_gan_safari.get_animals()
    # ramat_gan_safari.sort_animals()
    # ramat_gan_safari.get_groups()