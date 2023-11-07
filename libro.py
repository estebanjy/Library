import sqlite3

class Libro:    
    def __init__(self, titulo, autores, ISBN, genero, editorial, fechaPublicacion, resumen, imagen, usuarioPrestado):
        self.titulo = titulo
        self.autores = autores
        self.ISBN = ISBN
        self.genero = genero
        self.editorial = editorial
        self.fechaPublicacion = fechaPublicacion
        self.resumen = resumen
        self.imagen = imagen
        self.usuarioPrestado = usuarioPrestado
        self.historialPrestamos = self.verHistorialPrestamos()
        
    
    def verHistorialPrestamos(self):
        return self.historialPrestamos
        
    def verUsuarioPrestado(self):
        #aqui tienes que crear una funcion para que consulte a la base de datos quien tiene p
        return self.usuarioPrestado