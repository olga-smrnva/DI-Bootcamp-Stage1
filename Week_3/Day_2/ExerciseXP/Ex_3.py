# 1. Create a new python file and import your Dog class from the previous exercise.
import random

class Dog():
	def __init__(self, name, age, weight):
		self.name = name
		self.age = age
		self.weight = weight

	def bark(self):
		return f'{self.name} is barking'
	
	def run_speed(self):
		speed = self.weight/self.age*10
		return speed

	def fight(self, other_dog):
		if self.weight * self.run_speed() > other_dog.weight * other_dog.run_speed():
			return f'{self.name} wins'
		elif other_dog.weight * other_dog.run_speed() > self.weight * self.run_speed():
			return f'{other_dog.name} wins'
		else: 
			{'Drawn fight'}


# 2. In the new python file, create a class named PetDog that inherits from Dog.
# 3. Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.

class PetDog(Dog):
	def __init__(self, name, age, height, trained = False):
		super().__init__(name, age, height)
		self.trained = trained
# 4. Add the following methods:
#   * train: prints the output of bark and switches the trained boolean to True

	def train(self):
		print(self.bark())
		self.trained = True

#   * play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

	def play(self, *args):
		names = ', '.join(args)
		print(f'{names} all play together')

#   * do_a_trick: If the dog is trained the method should print one of the following sentences at random:
#       “dog_name does a barrel roll”.
#       “dog_name stands on his back legs”.
#       “dog_name shakes your hand”.
#       “dog_name plays dead”.

	def do_a_trick(self):
		commands = [' does a barrel roll', ' stands on his back legs', 'shakes your hand', 'plays dead']
		if self.trained == True:
			print(f'{self.name}{random.choice(commands)}')

dog1 = PetDog('Bobick', 4, 43)
dog1.train()
dog1.play('fff', 'sss', 'ddd')
dog1.do_a_trick()
