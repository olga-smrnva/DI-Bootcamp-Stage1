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
print(dog1.run_speed())
print(dog1.fight(dog2))

print(dog2.bark())
print(dog2.run_speed())
print(dog2.fight(dog3))

print(dog3.bark())
print(dog3.run_speed())
print(dog3.fight(dog1))