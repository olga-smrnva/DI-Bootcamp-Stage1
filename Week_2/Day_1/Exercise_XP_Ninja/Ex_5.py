previous_sent = ' '
record = 0

while len(previous_sent) != 0 :
	given_sent = input('Give me the longest sentence you can without the character “A” : \n')

	if record < len(given_sent) : 
		record = len(given_sent)
		print('Congrats! New sentence length record!')

	previous_sent = given_sent
	
	
