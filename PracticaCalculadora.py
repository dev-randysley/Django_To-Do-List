from tkinter import *

raiz = Tk()

raiz.title("Calculadora")

raiz.resizable(False,False)


miframe = Frame(raiz)

miframe.pack()

operacion =""

resultado = 0

OperacionAnterior =""

#-------------PANTALLA---------------------


numeropantalla = StringVar()

pantalla = Entry(miframe,bg="black",fg="green",justify = "right",font=("Arial",15),textvar=numeropantalla)

pantalla.grid(row=1,column=1,padx=1,pady=10,columnspan=4)


numeropantalla.set("0")
#------------PULSA BOTONES---------------
inicia = StringVar()


def NumeroPulsado(num):

	global operacion

	if(operacion != "" or numeropantalla.get() == "0") :

		numeropantalla.set(num)

		operacion =""

	else:
		numeropantalla.set(numeropantalla.get() + num)



def suma(num):

	global operacion,OperacionAnterior

	global resultado

	operacion = "suma"

	OperacionAnterior = operacion

	resultado += float(num)

	numeropantalla.set(resultado)



contadorresta = 0

def resta(num):

	global operacion,OperacionAnterior,resultado,contadorresta

	operacion = "resta"

	OperacionAnterior = operacion


	if( contadorresta == 0):

		resultado = float(num)

		contadorresta += 1

	else:

		if(OperacionAnterior == "resta"):

			resultado -= float(num)

		else:


			contadorresta == 0

	

	numeropantalla.set(resultado)

contadormulti = 0

def multiplica(num):

	global operacion,OperacionAnterior,resultado,contadormulti

	operacion = "multiplicacion"

	OperacionAnterior = operacion

	if(contadormulti == 0):

		resultado = float(num)

		contadormulti += 1

	else:

		if( OperacionAnterior == "multiplicacion"):

			resultado *= float(num)
		else:
			contadormulti = 0

	numeropantalla.set(resultado)

contadordivide = 0
num1 = 0.0

def divide(num):

	global operacion,OperacionAnterior,resultado,contadormulti,num1,contadordivide

	operacion = "division"

	OperacionAnterior = operacion
	num1 = float(num)

	if(contadordivide == 0):

		resultado = num1

		contadordivide += 1

	else:

		if( OperacionAnterior == "division" and num1 != 0):

			resultado /= num1
			numeropantalla.set(resultado)

		elif(OperacionAnterior == "division" and num1 == 0):

			numeropantalla.set("Error")
			contadordivide = 0

	


def Elresultado():

	global resultado,operacion,OperacionAnterior,contadorresta,contadordivide

	if(OperacionAnterior == "suma"):

		resultado += float(numeropantalla.get())

		numeropantalla.set(resultado)

	elif(OperacionAnterior =="resta"):

		resultado -= float(numeropantalla.get())

		numeropantalla.set(resultado)

	elif(OperacionAnterior == "multiplicacion"):

		resultado *= float(numeropantalla.get())

		numeropantalla.set(resultado)

	elif(OperacionAnterior == "division"):

		if (int(numeropantalla.get()) == 0):

			numeropantalla.set("Error")

		else:

			resultado /= float(numeropantalla.get())

			numeropantalla.set(resultado)

	resultado = 0
	contadorresta = 0
	contadormulti = 0
	contadordivide = 0


#--------------FILA 1 ---------------------

boton7 = Button(miframe,text="7",width=5,font=(10),command=lambda:NumeroPulsado("7"))
boton8 = Button(miframe,text="8",width=5,font=(10),command=lambda:NumeroPulsado("8"))
boton9 = Button(miframe,text="9",width=5,font=(10),command=lambda:NumeroPulsado("9"))
botondiv = Button(miframe,text="/",width=5,font=(10),command = lambda:divide(numeropantalla.get()))

boton7.grid(row=2,column=1)
boton8.grid(row=2,column=2)
boton9.grid(row=2,column=3)
botondiv.grid(row=2,column=4,pady=2)

#--------------FILA 2 ---------------------

boton6 = Button(miframe,text="6",width=5,font=(10),command=lambda:NumeroPulsado("6"))
boton5 = Button(miframe,text="5",width=5,font=(10),command=lambda:NumeroPulsado("5"))
boton4 = Button(miframe,text="4",width=5,font=(10),command=lambda:NumeroPulsado("4"))
botonx = Button(miframe,text="x",width=5,font=(10), command = lambda:multiplica(numeropantalla.get()))

boton6.grid(row=3,column=1,pady=2)
boton5.grid(row=3,column=2)
boton4.grid(row=3,column=3)
botonx.grid(row=3,column=4)

#--------------FILA 3 ---------------------

boton3 = Button(miframe,text="3",width=5,font=(10),command=lambda:NumeroPulsado("3"))
boton2 = Button(miframe,text="2",width=5,font=(10),command=lambda:NumeroPulsado("2"))
boton1 = Button(miframe,text="1",width=5,font=(10),command=lambda:NumeroPulsado("1"))
botonresta = Button(miframe,text="-",width=5,font=(10), command = lambda:resta(numeropantalla.get()))

boton3.grid(row=4,column=1,pady=2)
boton2.grid(row=4,column=2)
boton1.grid(row=4,column=3)
botonresta.grid(row=4,column=4)

#--------------FILA 4 ---------------------

boton0 = Button(miframe,text="0",width=5,font=(10),command=lambda:NumeroPulsado("0"))
botoncoma = Button(miframe,text=",",width=5,font=(10),command=lambda:NumeroPulsado("."))
botonigual = Button(miframe,text="=",width=5,font=(10),command=lambda:Elresultado())
botonsuma = Button(miframe,text="+",width=5,font=(10),command=lambda:suma(numeropantalla.get()))

boton0.grid(row=5,column=1,padx=2,pady=2)
botoncoma.grid(row=5,column=2,padx=2)
botonigual.grid(row=5,column=3,padx=2)
botonsuma.grid(row=5,column=4,padx=2)

#------------BOTON BORRAR-------------------------

def borrar():

	global resultado,contadormulti,contadorresta,contadordivide

	numeropantalla.set("")
	resultado = 0
	contadormulti = 0
	contadorresta = 0
	contadordivide =0

botonborrar = Button(miframe,text="Ce",font=(10),width=12,command=borrar)
botonborrar.grid(row=6,column=1,columnspan=2)



raiz.mainloop()