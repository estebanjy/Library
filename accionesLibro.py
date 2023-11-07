import sqlite3
from abc import ABC, abstractmethod


class Acciones(ABC):
    
    def verLibrosDisponibles():
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        libros = cursor.execute("""SELECT Titulo FROM Libros
        WHERE IDUsuarioNormal IS NULL""")
        cursor.close()
        conexion.close()
        resultado = libros.fetchall()
        #aqui se tiene que crear algo para poder mostrarlo despues en el visual
        return resultado

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
    
    def verLibrosTomados(libros):
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        libros = cursor.execute("""SELECT Titulo FROM Libros
        WHERE IDUsuarioNormal IS NOT NULL""")
        cursor.close()
        conexion.close()
        resultado = libros.fetchall()
        #aqui se tiene que crear algo para poder mostrarlo despues en el visual
        return resultado
        
        
class AccionesUsuarioNormal(Acciones):
    #estas acciones tienen que estar enlazadas a una cuenta admin
    def pedirLibro(UsuarioNormal, libro):
        #Aqui primero se tendria que mostrar al usuario todos los libros disponibles
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        cursor.execute("""UPDATE Libros
        SET IDUsuarioNormal = ? 
        WHERE ISBN = ?
        """,(UsuarioNormal.IDUsuarioNormal, libro.ISBN))
        conexion.commit()
        cursor.execute()
        conexion.execute()
    
    def devolverLibro(UsuarioNormal, libro):
        #Aqui se necesita algo para que el usuartio pueda elegir que libro quiere devolver
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        cursor.execute("""UPDATE Libros
        SET IDUsuarioNormal = NULL 
        WHERE ISBN = ?
        """,(UsuarioNormal.IDUsuarioNormal, libro.ISBN))
        conexion.commit()
        cursor.execute()
        conexion.execute()