magicNum = 6 
no = 0; 
guess = input('Guess a number from 1 to 10. (please enter 0 if you wish to end this simulation.):')
guess = int(guess)
while (guess != magicNum) and (guess != no): 
	if (guess > 10) or (guess < no):
		print('That is not a number from 1 to 10!')  
	elif (guess > magicNum) and (guess != no):
		print('That is too high!')
	else:
		print('That is too low!')

	guess = input('Guess again! (Number from 1 to 10, 0 to end.):')
	guess = int(guess)


if guess == magicNum:
	print ('That is correct')

print ('End Simulation')

	
