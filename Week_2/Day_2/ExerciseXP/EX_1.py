# 1. Create a set called my_fav_numbers with all your favorites numbers.
my_fav_numbers = {3,7,11,27,13579}

# 2. Add two new numbers to the set.
my_fav_numbers.add(15)
my_fav_numbers.add(77)

# 3. Remove the last number.
my_list = list(my_fav_numbers)[:-1]
my_fav_numbers = set(my_list)

# 4. Create a set called friend_fav_numbers with your friend’s favorites numbers.
friend_fav_numbers = {4,8,88,45,678}

# 5. Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(my_fav_numbers)
print(friend_fav_numbers)
print(our_fav_numbers)
