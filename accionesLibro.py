import sqlite3
from libro import Libro
from abc import ABC, abstractmethod

class Acciones(ABC):  
    
    def verLibrosDisponibles(self):
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        libros = cursor.execute("""SELECT Imagen, Titulo, Autores, Genero, Editorial, Resumen FROM Libros
        WHERE IDUsuarioNormal IS NULL""")
        resultado = libros.fetchall()
        cursor.close()
        conexion.close()
        #aqui se tiene que crear algo para poder mostrarlo despues en el visual
        return resultado 
    
    
    def verDatosGeneralesLibro(libro):
        titulo = libro.titulo
        autores = libro.autores
        isbn = libro.ISBN
        genero = libro.genero
        editorial = libro.editorial
        fechaPublicacion = libro.fechaPublicacion
        resumen = libro.resumen
        imagen = libro.imagen
        usuarioPrestado = libro.usuarioPrestado
    
    
class AccionesAdministrador(Acciones): 
    #hay que hacer algo para que las acciones de administrador esten enlasadas con una cuenta admin 
    def guardarlibro(libro):
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        cursor.execute("""INSERT INTO Libros(Titulo, Autores, ISBN, Genero, Editorial, FechaPublicacion, Resumen, Imagen)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,(libro.titulo, libro.autores, libro.ISBN, libro.genero, libro.editorial, libro.fechaPublicacion, libro.resumen, libro.imagen))
        conexion.commit()
        cursor.close()
        conexion.close()
        
    def eliminarLibro(libro):
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        cursor.execute("""DELETE FROM Libros WHERE ISBN = ?""", (libro.ISBN, ))
        conexion.commit()
        cursor.close()
        conexion.close()
    
    def verLibrosTomados():
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        libros = cursor.execute("""SELECT Titulo FROM Libros
        WHERE IDUsuarioNormal IS NOT NULL""")
        resultado = libros.fetchall()
        cursor.close()
        conexion.close()
        #aqui se tiene que crear algo para poder mostrarlo despues en el visual
        return resultado
    
    def verHistorialPrestamosLibro(libro):
        pass
        
class AccionesUsuarioNormal(Acciones):

    def verLibrosTomados(IDUsuarioNormal):
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        libros = cursor.execute("""SELECT Imagen, Titulo, Autores, Genero, Editorial, Resumen FROM Libros
        WHERE IDUsuarioNormal IS ?""",(IDUsuarioNormal,))
        libros = libros.fetchall()
        cursor.close()
        conexion.close()
        #En esta parte no es una buena practica devolver una lista por lo cual hay que buscar una forma de devolver esto sin perjudicar esto
        return libros
        
    #estas acciones tienen que estar enlazadas a una cuenta usuario
    #aqui hay que desempaquetar el libro para que se pueda hacer la operacion
    def pedirLibro(UsuarioNormal, libro):
        #En esta parte hay que entregarle el objeto de UsuarioNormal si o si los datos del usuario de la base de datos
        #Aqui primero se tendria que mostrar al usuario todos los libros disponibles
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor() 
        registro = cursor.execute("""SELECT HistorialPrestamos FROM Libros 
        WHERE ISBN = ?""", (libro.ISBN, ))
        resultado = registro.fetchone()
        resultado = resultado[0] 
        if resultado == None:
            resultado = ""

        cursor.execute("""UPDATE Libros
        SET IDUsuarioNormal = ?, HistorialPrestamos = ?
        WHERE ISBN = ?
        """,(UsuarioNormal.IDUsuarioNormal,resultado + UsuarioNormal.IDUsuarioNormal + ", ", libro.ISBN))
        
        conexion.commit()
        cursor.close()
        conexion.close()
    
    #hay que crear una metodo que muestre todos los libros que tiene prestado el usuario 
    def devolverLibro(libro):
        #Aqui se necesita algo para que el usuario pueda elegir que libro quiere devolver 
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        cursor.execute("""UPDATE Libros
        SET IDUsuarioNormal = NULL 
        WHERE ISBN = ?""",(libro.ISBN, ))
        conexion.commit()
        cursor.close()
        conexion.close()
s = AccionesAdministrador()
resultado = s.verLibrosDisponibles()
print(resultado)