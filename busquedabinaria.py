
def binary_search(numbers,number_to_find,low,hight):


	if low > hight: # debe ir si vamos aplicar recursividad, caso base!!

		return False

	mid = int((low + hight) / 2)

	if numbers[mid] == number_to_find:

		return True

	elif numbers[mid] > number_to_find:
		
		return binary_search(numbers,number_to_find,low,mid -1)	

	else:

		return binary_search(numbers,number_to_find,mid + 1,hight)





if __name__ =='__main__':

	numbers =[1,3,4,6,9,10,12,18,20,34,55,77]

	number_to_find =int(input("Ingresa un numero: "))

	result = binary_search(numbers,number_to_find,0,len(numbers) - 1)

	if result is True:

		print("Numero encontrado")

	else:

		print("No se encontro el numero")
