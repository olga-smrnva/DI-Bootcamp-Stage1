# 1
import random

print("Hey, give me a 10 characters long string")
given_string = input()

if len(given_string) > 10 : print("string too long")
else : print("string too short")

# 2
firstChar = given_string[0]
lastChar = given_string[len(given_string) - 1]
print(firstChar)
print(lastChar)

# 3
for letter in range(1, len(given_string) + 1) : print(given_string[:letter])

# 4
l = list(given_string)
random.shuffle(l)
print(''.join(l))