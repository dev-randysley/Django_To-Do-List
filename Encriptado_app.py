def app():


	KEYS ={'a':'1','b':'2','c':'3','d':'4',

		   'e':'5','f':'6','g':'7','h':'8',

		   'i':'9','j':'a','k':'b','l':'x',

		   'm':'d','n':'e','o':'f','p':'g',

		   'q':'h','r':'i','s':'j','t':'k',

		   'u':'m','v':'n','w':'0','x':'p',

		   'y':'q','z':'r'
	}

	while True:

		command = raw_input("\nIngrese la accion a realizar: [e]ncritado , [d]esencriptado , [s]alir: ")

		if command == 'e':

			word = raw_input("\nIngrese la palabra a encriptar: ")

			word_encriptada = encriptado(word,KEYS)

			print('\nLa palabra Encriptada es: {}'.format(word_encriptada))

		elif command == 'd':

			word = raw_input("\nIngrese la palabra a desencriptar: ")

			word_desencriptada = desencriptado(word,KEYS)

			print('\nLa palabra Desencriptada es: {}'.format(word_desencriptada))

		elif command == 's':

			print('\nSaliendo...')
			quit()

		else:

			print('Comando invalido..\n')

def encriptado(word,KEYS):

	words = word.split(' ')

	words_encriptadas = []

	for word in words:

		word_encriptada =''

		for letter in word:

			word_encriptada += KEYS[letter]

		words_encriptadas.append(word_encriptada)

	return ' '.join(words_encriptadas)

	

def desencriptado(word,KEYS):


	words = word.split(' ')

	words_desencriptadas = []

	for word in words:

		word_desencriptada = ''

		for letter in word:

			for key,value in KEYS.items():

				if letter == value:

					word_desencriptada += key

		words_desencriptadas.append(word_desencriptada)

	return ' '.join(words_desencriptadas)


if __name__ == '__main__':

	print("PROGRAMA DE ENCRIPTADO")

	app()