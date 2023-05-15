#1. Create a class called Family and implement the following attributes:

# 		* members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# 		* last_name : (string)

members = [
		{'name':'Michael','age':35,'gender':'Male','is_child':False},
		{'name':'Sarah','age':32,'gender':'Female','is_child':False}
		]
last_name = 'Smith'

class Family():
	
	def __init__(self, members, last_name):
		self.members = members
		self.last_name = last_name

#2. Implement the following methods:

# 	* born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.

	def born(self, **kwargs):
		self.members.append(kwargs)
		print('Congrast! There\'s a newborn!')

# 	* is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.

	def is_18(self, name):
		for member in self.members:
			if member['name'] == name:
				return member['age'] >= 18
		
		print(f'There\'s no such a member {name}')

# 	* family_presentation: a method that prints the family’s last name and all the members’ first name.

	def family_presentation(self):
		print(f'The family {self.last_name} members are: ')
		for member in self.members:
			print(member['name'])

family1 = Family(members, last_name)
family1.born(name='Harry',age=0,gender='Male',is_child=True)
print(family1.is_18('Harry'))
family1.family_presentation()