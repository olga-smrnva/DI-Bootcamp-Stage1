class Cat:
	def __init__(self, cat_name, cat_age):
		self.name = cat_name
		self.age = cat_age

# 1. Instantiate three Cat objects using the code provided above.

cat1 = Cat('Sussy', 3)
cat2 = Cat('Murmur', 7)
cat3 = Cat('Puss', 4)

# 2. Outside of the class, create a function that finds the oldest cat and returns the cat.

def get_oldest_cat(cat1, cat2, cat3):
	oldest = max(cat1.age, cat2.age, cat3.age)
	if oldest ==  cat1.age : return (f"The oldest cat is {cat1.name} {cat1.age} years old.")
	elif oldest == cat2.age : return (f"The oldest cat is {cat2.name} {cat2.age} years old.")
	elif oldest == cat3.age : return (f"The oldest cat is {cat3.name} {cat3.age} years old.")

# 3. Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

print(get_oldest_cat(cat1, cat2, cat3))
