# 1. Create a class called Farm. How should it be implemented?
# 2. Does the Farm class need an __init__ method? If so, what parameters should it take?
# 3. How many methods does the Farm class need?
# 4. Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# 5. Test your code and make sure you get the same results as the example above.

class Farm:
	def __init__(self, farm_name):
		self.name = farm_name
		self.animals = {}
		self.count = 0
		
	def add_animal(self, animal_name, count=1):
		if not self.animals.get(animal_name) :
			self.animals[animal_name] = count
		else : 
			self.animals[animal_name] = self.animals[animal_name] + count

	def get_info(self):
		message = f'{self.name}`s farm \n\n' 
		for animal, count in self.animals.items():
			message += f'{animal} : {count} \n'
		message += '\n    E-I-E-I-0!'
		return message
	
# 6. Bonus: nicely line the text in columns as seen in the example above. Use string formatting.

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())