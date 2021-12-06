# -*- coding: utf-8 -*-


from Tkinter import *

from Tkinter import messagebox
import sqlite3


raiz = Tk()

raiz.title("Base de Datos")
frame = Frame(raiz,width =1200, height =500)
frame.pack()

IDd = StringVar()
nombre = StringVar()
apellido = StringVar()
direccion = StringVar()
contrasena = StringVar()


#---------------------------ID---------------------------------------------
Label(frame,text ="Id: ",font=("Arial",15)).grid(row = 1, column = 1,pady= 10)

idText = Entry(frame,justify ="center", textvariable = IDd)
idText.grid(row = 1, column = 2,pady=10)


#---------------------------NOMBRE----------------------------------------------

Label(frame, text = "Nombre: ", font=("Arial",15)).grid(row= 2, column= 1,pady=10)
nombreText = Entry(frame,justify ="center",textvariable = nombre)
nombreText.grid(row=2 , column = 2,pady = 10)

#---------------------------------APELLIDO-----------------------------------

Label(frame, text = "Apellido: ", font=("Arial",15)).grid(row = 3, column = 1, pady = 10)
apellidoText = Entry(frame,justify ="center",textvariable = apellido)
apellidoText.grid(row = 3,column = 2, pady = 10)


#----------------------------CONTRASEÑA-------------------------------------

Label(frame,text = "Password: ", font=("Arial",15)).grid(row = 4, column = 1, pady = 10)
passText = Entry(frame,justify ="center",textvariable = contrasena,show ="*")
passText.grid(row = 4, column = 2, pady = 10)

#--------------------------------------DIRECCION-----------------------------------

Label(frame, text ="Dirección: ",  font=("Arial",15)).grid(row = 5, column = 1, pady = 10)
direccionText = Entry(frame,justify ="center",textvariable = direccion)
direccionText.grid(row= 5, column = 2,pady = 10)

#------------------------COMENTARIOS-------------------------------------------------------------------------

Label(frame, text = "Comentarios: ",  font=("Arial",15)).grid(row = 6, column = 1)

comentarioText = Text(frame,width = 16, height = 5)

comentarioText.grid(row=6, column = 2)

ruedaComentario = Scrollbar(frame,command=comentarioText.yview)

ruedaComentario.grid(row = 6 , column =3,sticky="nsew")

comentarioText.config(yscrollcommand=ruedaComentario.set)

#--------------------------funciones------------------------------------

def conectar():

	try:

		Conexion = sqlite3.connect("BBDD practica")
		MiCursor = Conexion.cursor()

		MiCursor.execute("CREATE TABLE Datos_Usuarios (ID INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE VARCHAR(50), APELLIDO VARCHAR(50), CONTRASEÑA VARCHAR(50), DIRECCION VARCHAR(50),COMENTARIOS VARCHAR(100))")

		messagebox.showinfo("Información","BBDD Creada con Exito" )
	except:
		
		messagebox.showwarning("Alerta", "BBDD ya creada")
	
	finally:

		Conexion.commit()

		Conexion.close()	

def crear():

	
	try:

		Conexion = sqlite3.connect("BBDD practica")
		MiCursor = Conexion.cursor()

		datos = (nombre.get(),apellido.get(),contrasena.get(),direccion.get(),comentarioText.get("1.0",END))

		#MiCursor.execute("INSERT INTO Datos_Usuarios VALUES(null,'" + nombre.get() + "','" + apellido.get() + "','" + contraseña.get() + "','" + dirección.get() + "','" + comentarioText.get("1.0",END) + "')")

		MiCursor.execute("INSERT INTO Datos_Usuarios VALUES(NULL,?,?,?,?,?)",datos)


		messagebox.showinfo("Informacion","Se inserto un registro a la BBDD")

	except:
		messagebox.showwarning("Alerta","No se pudo insertar el registro")

	finally:

		Conexion.commit()

		Conexion.close()	

def salir():

	valor = messagebox.askquestion("Salir","¿Desea Salir de la aplicación?")

	if valor == "yes":

		raiz.destroy()



def borrarcampos():

	nombre.set("")
	apellido.set("")
	contrasena.set("")
	direccion.set("")
	IDd.set("")
	comentarioText.delete(1.0,END)


def leer():

	try:

		conexion = sqlite3.connect("BBDD practica")

		cursor = conexion.cursor()

		cursor.execute("SELECT * FROM Datos_Usuarios WHERE ID = '" + IDd.get() + "' ")

		vector = cursor.fetchall()



		for elemento in vector:

			nombre.set(elemento[1])
			apellido.set(elemento[2])
			contrasena.set(elemento[3])
			direccion.set(elemento[4])
			comentarioText.delete(1.0,END)
			comentarioText.insert(1.0,elemento[5])

			break



	except:

		messagebox.showwarning("Aviso","La Informacion no se pudo recuperar")

	finally:

		conexion.commit()

		conexion.close()	


def actualizar():

	conexion = sqlite3.connect("BBDD practica")

	cursor = conexion.cursor()

	datos = (nombre.get(),apellido.get(),contrasena.get(),direccion.get(),comentarioText.get("1.0",END))

	"""cursor.execute("UPDATE Datos_Usuarios SET NOMBRE = '" + nombre.get() +  "', APELLIDO = '" + apellido.get() + 
		"' ,CONTRASEÑA = '" + contraseña.get() + "', DIRECCION = '" + dirección.get() + 
		"',COMENTARIOS = '" + comentarioText.get("1.0",END) + "' WHERE ID = " + IDd.get())  """

	cursor.execute("UPDATE Datos_Usuarios SET NOMBRE = ?, APELLIDO =?, CONTRASEÑA = ?, DIRECCION = ?, COMENTARIOS = ? " +
		"WHERE ID =" + IDd.get(),datos)

	conexion.commit()

	messagebox.showinfo("Aviso","Registro actualizado")
	conexion.close()



def borrar():

	conexion = sqlite3.connect("BBDD practica")

	cursor = conexion.cursor()

	cursor.execute("DELETE FROM Datos_Usuarios WHERE ID = '" + IDd.get() + "'  ")

	conexion.commit()

	messagebox.showinfo("Aviso","Registro eliminado de la Base de Datos")

	conexion.close()


#--------------------------------BOTONES----------------------------------------

frame2 = Frame(raiz)
frame2.pack()

botoncrear = Button(frame2,text="Crear", command = crear)
botoncrear.grid(row = 0 , column = 0,padx=10,pady = 5)

botonleer = Button(frame2,text="Leer", command = leer)
botonleer.grid(row= 0, column = 1,padx = 10)

botonActualizar = Button(frame2, text = "Actualizar", command = actualizar)
botonActualizar.grid(row = 0, column = 2, padx = 10)

botonBorrar = Button(frame2, text = "Borrar", command = borrar)
botonBorrar.grid(row = 0, column = 3, padx = 10)

#---------------------MENU-------------------------------------------------------

BarraMenu = Menu(raiz)

raiz.config(menu = BarraMenu, width = 300, height = 300)

archivo = Menu(BarraMenu,tearoff = 0)
borrar = Menu(BarraMenu,tearoff = 0)
CRUD = Menu(BarraMenu,tearoff = 0)
ayuda= Menu(BarraMenu,tearoff = 0)

BarraMenu.add_cascade(label = "BBDD" , menu = archivo)
BarraMenu.add_cascade(label ="Borrar", menu = borrar)
BarraMenu.add_cascade(label ="CRUD", menu = CRUD)
BarraMenu.add_cascade(label ="Ayuda", menu = ayuda)


archivo.add_command(label ="Conectar", command = conectar)
archivo.add_command(label ="Salir", command = salir)

borrar.add_command(label ="Borrar Campos", command = borrarcampos)

CRUD.add_command(label ="Crear", command = crear)
CRUD.add_command(label ="Leer", command = leer)
CRUD.add_command(label ="Actualizar", command = actualizar)
CRUD.add_command(label ="Borrar", command = borrar)


ayuda.add_command(label ="Licencia")
ayuda.add_command(label ="Acerca de...")

#-------------------------------------------------


















raiz.mainloop()