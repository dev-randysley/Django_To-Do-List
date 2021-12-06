import random

IMAGES = ['''


	+----+
	|    |
		 |
		 |
		 |
		 |
		 |
		 ========''', '''


	+----+
	|    |
	O	 |
		 |
		 |
		 |
		 |
		 ========''', '''


	+----+
	|    |
	O	 |
	|	 |
		 |
		 |
		 |
		 ========''','''



    +----+
	|    |
	O	 |
   /|	 |
		 |
		 |
		 |
		 ========''','''


	+----+
	|    |
	O	 |
   /|\	 |
		 |
		 |
		 |
		 ========''','''



   +----+
	|    |
	O	 |
   /|\	 |
	|	 |
		 |
		 |
		 ========''','''


    +----+
	|    |
	O	 |
   /|\	 |
	|	 |
   /	 |
		 |
		 ========''','''


   +----+
	|    |
	O	 |
   /|\	 |
	|	 |
   / \	 |
		 |
		 ========'''



]


WORDS =['lavadora','secadora','sofa','gobierno','diputado','computadora','teclado','casa']

def randon_word():

	idx = random.randint(0,len(WORDS) -1)

	return WORDS[idx]

def display_board(hidden_word,tries):

	print(IMAGES[tries])

	print('')

	print(hidden_word)

	print('----*-----*-----*-----*-----*-----*-----*-----')


def run():

	word = randon_word() 

	hidden_word = ['-'] * len(word)

	tries = 0

	count = 0

	letter_use =[]

	inicio = True

	while True:

		display_board(hidden_word,tries)

		
		current_letter = raw_input("Escoge una letra: ")
	

		letter_indexes = []

		for idx in range(len(word)):

			if word[idx] == current_letter:

				letter_indexes.append(idx)

		if len(letter_indexes) == 0:

			tries += 1


			if tries == 7:

				display_board(hidden_word,tries)
				print('')
				print("Perdiste la palabra correcta era {}".format(word))

				break
		else:

			for idx in letter_indexes:

				hidden_word[idx] = current_letter

			letter_indexes =[]


		try:
			hidden_word.index('-')

		except:

			print("Haz Ganado!! la palabra es {}".format(word))	

			break





if __name__=='__main__':

	print('A H O R C A D O S')


	run()
