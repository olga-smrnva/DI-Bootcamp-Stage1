matrix = [[
   '7',
   'T',
   'h',
   'i',
   's',
   '$',
   '#',
   '^'
], [
   'i',
   's',
   '%',
   ' ',
   'M',
   'a',
   't',
   'r',
], [
   'i',
   'x',
   '#',
   ' ',
   ' ',
   '%',
   '!',

]]

def descript_matrix(matrix:list):
   message = ''
   for column in matrix:
       for char in column:
           if char.isalpha():
               message += char
           elif message and message[-1] != ' ':
               message += ' '
   return message

print(descript_matrix(matrix))

