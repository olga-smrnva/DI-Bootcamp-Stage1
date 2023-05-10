# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
import random

def compare_numbers(num) :
    num = int(num)
    if num < 1 or num > 100 : return False
    
    second_num = random.randint(1,100)
    if num == second_num :
        print(f'Success, numbers are the same: {num, second_num}')
    else : print(f'Failure, numbers are different: {num, second_num}')
    
    
compare_numbers(44)