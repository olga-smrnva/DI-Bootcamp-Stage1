#___________________________________
# 1

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

#___________________________________
# 2

# 1. Create a class called Dog with the following attributes name, age, weight.

class Dog():
	def __init__(self, name, age, weight):
		self.name = name
		self.age = age
		self.weight = weight

# 2. Implement the following methods in the Dog class:
#	* bark: returns a string which states: “<dog_name> is barking”.

	def bark(self):
		return f'{self.name} is barking'
	
#	* run_speed: returns the dogs running speed (weight/age*10).

	def run_speed(self):
		speed = self.weight/self.age*10
		return speed

#	* fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

	def fight(self, other_dog):
		if self.weight * self.run_speed() > other_dog.weight * other_dog.run_speed():
			return f'{self.name} wins'
		elif other_dog.weight * other_dog.run_speed() > self.weight * self.run_speed():
			return f'{other_dog.name} wins'
		else: 
			{'Drawn fight'}

# 3. Create 3 dogs and run them through your class.

dog1 = Dog('Bobick', 4, 43)
dog2 = Dog('Rex', 7, 34)
dog3 = Dog('Chubby', 2, 88)

print(dog1.bark())


#___________________________________
# 3