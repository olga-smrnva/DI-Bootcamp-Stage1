print('Please, enter the moths using its order number (from 1 to 12)')
month_number = int(input())

if month_number == 3 or month_number == 4 or month_number == 5 :
    print('This is Spring')
elif month_number >= 6 and month_number <=8 :
    print('This is Summer')
elif month_number >= 9 and month_number <=11 :
    print('This is Autumn')
elif month_number == 1 or month_number == 2 or month_number == 12 :
    print('This is Winter')
    
else : print('Oooopsey, wrong number')
