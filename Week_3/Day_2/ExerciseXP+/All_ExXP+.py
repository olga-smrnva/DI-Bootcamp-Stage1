#___________________________________
# 1

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

#___________________________________
# 2

class Family():
	
	def __init__(self, members, last_name):
		self.members = members
		self.last_name = last_name

	def born(self, **kwargs):
		self.members.append(kwargs)
		print('Congrast! There\'s a newborn!')

	def is_18(self, name):
		for member in self.members:
			if member['name'] == name:
				return member['age'] >= 18

		print(f'There\'s no such a member {name}')

	def family_presentation(self):
		print(f'The family {self.last_name} members are: ')
		for member in self.members:
			print(member['name'])


# 1. Create a class called TheIncredibles. This class should inherit from the Family class:

members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]
last_name = 'Smith'

class TheIncredibles(Family):		

# 2.Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.

	def use_power(self, member):
		if member['age'] >= 18 :
			try:
				print(f'{member["name"]} has a {member["power"]} power')
			except:
				print('They are not over 18 years old')

# 3. Add a method called incredible_presentation which : * prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method) * prints all the members’ incredible name and power.

	def incredible_presentation(self):
		super().family_presentation()
		for member in self.members:
			print(f'{member["name"]} has a {member["power"]} power')

# 5. Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.

	def incredible_born(self, **kwargs):
		super().born( **kwargs)


# 4. Call the incredible_presentation method.

family1 = TheIncredibles(members, last_name)
family1.incredible_presentation()
family1.incredible_born(name='Jack',age=0,gender='Male',is_child=True,power='unknown')

# 6. Call the incredible_presentation method again.
family1.incredible_presentation()