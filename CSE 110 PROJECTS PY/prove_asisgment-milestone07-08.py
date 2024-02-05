import random
# library that we use in order to choose on random secret_words from a list of secret_words

name = input('What is your name? ')

# Here the user is asked to enter the name first

print(f'Welcome to the word guessing game! {name}')

secret_words = ['which', 'there', 'their', 'about', 'would', 'these', 'other', 'words', 'could',
                'first', 'water', 'after', 'where', 'right', 'think', 'three', 'years', 'place', 'sound',
                'great', 'again', 'still', 'every', 'small', 'found', 'those', 'never', 'under', 'might',
                'while', 'house', 'world', 'below', 'asked', 'going', 'large', 'until', 'along', 'shall',
                'being', 'often', 'earth', 'began', 'since', 'study', 'night', 'light', 'above', 'paper',
                'parts', 'young', 'story', 'point', 'times', 'heard', 'whole', 'white', 'given', 'means',
                'music', 'miles', 'thing', 'today', 'later', 'using', 'money', 'lines', 'order', 'group',
                'among', 'learn', 'known', 'space', 'table', 'early', 'trees', 'short', 'hands', 'state',
                'black', 'shown', 'stood', 'front', 'voice', 'kinds', 'makes', 'comes', 'close', 'power',
                'lived', 'vowel', 'taken', 'built', 'heart', 'ready', 'quite', 'class', 'bring', 'round',
                'horse', 'shows', 'piece', 'green', 'stand', 'birds', 'start', 'river', 'tried', 'least',
                'field', 'whose', 'girls', 'leave', 'added', 'color', 'third', 'hours', 'moved', 'plant',
                'doing', 'names', 'forms', 'heavy', 'ideas', 'cried', 'check', 'floor', 'begin', 'woman',
                'alone', 'plane', 'spell', 'watch', 'carry', 'wrote', 'clear', 'named', 'books', 'child',
                'glass', 'human', 'takes', 'party', 'build', 'seems', 'blood', 'sides', 'seven', 'mouth',
                'solve', 'north', 'value', 'death', 'maybe', 'happy', 'tells', 'gives', 'looks', 'shape',
                'lives', 'steps', 'areas', 'sense', 'speak', 'force', 'ocean', 'speed', 'women', 'metal',
                'south', 'grass', 'scale', 'cells', 'lower', 'sleep', 'wrong', 'pages', 'ships', 'needs', ]

game = True
while game:
	# Function will choose one random word from this list of secret_words
	word = random.choice(secret_words)
	attempt = ''
	turns = 5  # any number of turns can be used here
	while turns > 0:
		failed = 0  # counts the number of times a user fails
		for letter in word:  # all characters from the input word taking one at a time.
			if letter in attempt:  # comparing that character with the character in attempt
				print(*letter.capitalize(), end=' ')
			else:
				print(end=' _ ')

				failed += 1  # for every failure 1 will beincremented in failure

		if failed == 0:
			# user will win the game if failure is 0 and 'You Win' will be given as output
			print('Congratulations! You guessed it!')
			# this print the correct word
			print('It took you', + turns-(-2), 'guesses.')

		print()  # if user has input the wrong alphabet then it will ask user to enter another alphabet
		guess = input('What is your guess?: ')
		attempt += guess  # every input character will be stored in attempt

		if guess not in word:  # check input with the character in word
			turns -= 1
			# if the character doesn’t match the word then “Wrong” will be given as output
			print('Your guess was not correct.')
			# this will print the number of turns left for the user
			print('You have', + turns, 'more attempt')

			if turns == 0:
				print('You Loose :( End of Game, the correct word is', word.upper())

	play = True
	while play:

		play_again = input('Do you want to play again? (Y/N) ')

		if play_again.lower() == "y":
			print("This is the new secret word!")
			play = False
		elif play_again.lower() == "n":
			print(f"Thanks for playing {name}!")
			play = False
			game = False
		else:
			print("Please enter a correct input 'y' or 'n'")