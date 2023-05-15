# 1. Create a class called Zoo.

# 2. In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).

class Zoo:
	def __init__(self, zoo_name):
		self.animals = set()
		self.name = zoo_name

# 3. Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.

	def add_animal(self, new_animal): 
		self.animals.add(new_animal)
		

# 4. Create a method called get_animals that prints all the animals of the zoo.

	def get_animals(self):
		print(*(self.animals), sep=', ')



# 5. Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.

	def sell_animal(self, animal_sold):
		if animal_sold in self.animals:
			self.animals.remove(animal_sold)


# 6. Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.

	def sort_animals(self):
		sorted_list = list(self.animals)
		sorted_list.sort()
		sorted_animals = {}
		i = 0
		current_letter = ''

		for animal in sorted_list:
			if animal[0] != current_letter:
				i += 1
				sorted_animals[i] = animal
				current_letter = animal[0]
			else:
				if type(sorted_animals[i]) == list:
					sorted_animals[i].append(animal)
				else:
					sorted_animals[i] = [sorted_animals[i], animal]
		return sorted_animals


# 7. Create a method called get_groups that prints the animal/animals inside each group.

	def get_groups(self):
		sorted_animals = self.sort_animals()
		print('Groups:')
		
		for k, v in sorted_animals.items():
			print (f'{k}: {v}')


# 8. Create an object called ramat_gan_safari and call all the methods.

ramat_gan_safari = Zoo('Ramat Gan Safari')

while True:
	new_animal = input('Which animal do you want to see in our zoo? Type here (print "quit" to stop): \n')
	if new_animal == 'quit': 
		break
	ramat_gan_safari.add_animal(new_animal)

ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('monkey')
ramat_gan_safari.get_animals()
ramat_gan_safari.get_groups()
