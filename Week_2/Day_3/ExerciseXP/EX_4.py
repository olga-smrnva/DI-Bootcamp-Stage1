users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# 1. Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.

disney_users_A = {}
number = 0

for user in users:
    disney_users_A[user] = number
    number += 1
    
print(disney_users_A)

# 2. Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.

disney_users_B = {}
number = 0

for user in users:
    disney_users_B[number] = user
    number += 1
    
print(disney_users_B)

# 3. Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.

sorted_users = users[:]
sorted_users.sort()

number = 0
disney_users_C = {}

for user in sorted_users:
    disney_users_C[user] = number
    number += 1

print(disney_users_C)

# 4. Only recreate the 1st result for:
#	*The characters, which names contain the letter “i”.

disney_users_A_copy1 = disney_users_A.copy()

for user in users :
    if 'i' not in user : 
        del disney_users_A_copy1[user]
        
print(disney_users_A_copy1)

#	*The characters, which names start with the letter “m” or “p”.

disney_users_A_copy2 = disney_users_A.copy()

for user in users:
    if not user.startswith('P') and not user.startswith('M') :
        del disney_users_A_copy2[user]
        
print(disney_users_A_copy2)

