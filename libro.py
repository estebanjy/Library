import sqlite3
#from accionesLibro import AccionesAdministrador

class Libro:    
    def __init__(self, titulo, autores, ISBN, genero, editorial, fechaPublicacion, resumen, imagen):
        self.titulo = titulo
        self.autores = autores
        self.ISBN = ISBN
        self.genero = genero
        self.editorial = editorial
        self.fechaPublicacion = fechaPublicacion
        self.resumen = resumen
        self.imagen = imagen
        
#l = Libro("el hobbit", "asd", "asdsad", "accion", "asdd", "asdasd", " aksdjsa", "asdlkj")
#AccionesAdministrador.guardarlibro(l)