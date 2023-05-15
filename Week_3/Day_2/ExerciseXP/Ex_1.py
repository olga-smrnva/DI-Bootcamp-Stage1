class Pets():
	def __init__(self, animals):
		self.animals = animals

	def walk(self):
		for animal in self.animals:
			print(animal.walk())

class Cat():
	is_lazy = True

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def walk(self):
		return f'{self.name} is just walking around'

class Bengal(Cat):
	def sing(self, sounds):
		return f'{sounds}'

class Chartreux(Cat):
	def sing(self, sounds):
		return f'{sounds}'


# 1. Create another cat breed named Siamese which inherits from the Cat class.

class Siamese(Cat):
	def sing(self, sounds):
		return f'{sounds}'

# 2. Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
cat1 = Siamese('Harry', 11)
cat2 = Chartreux('Ella', 6)
cat3 = Bengal('Tom', 1)

all_cats = []
all_cats.extend([cat1, cat2, cat3])


# 3. Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.

sara_pets = Pets(all_cats)

# 4. Take all the cats for a walk, use the walk method.

sara_pets.walk()