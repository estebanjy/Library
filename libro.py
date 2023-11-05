class Libro:
    def __init__(self, titulo, autores, ISBN, genero, editorial, fechaPublicacion, resumen, imagen, UsuarioPrestado):
        self.titulo = titulo
        self.autores = autores
        self.ISBN = ISBN
        self.genero = genero
        self.editorial = editorial
        self.fechaPublicacion = fechaPublicacion
        self.resumen = resumen
        self.imagen = imagen
        self.UsuarioPrestado = UsuarioPrestado
        self.historialPrestamos = self.verHistorialPrestamos()

    def verHistorialPrestamos(self):
        #aqui tienes que crear una ruta para que se consulte en la base de datos el historial de prestamos
        pass
    
    def verUsuarioPrestado():
        #aqui tienes que crear una funcion para que consulte a la base de datos quien tiene p
        pass

class s(Libro):
    def __init__(self, titulo, autores, ISBN, genero, editorial, fechaPublicacion, resumen, imagen, UsuarioPrestado, historialPrestamos):
        super().__init__(titulo, autores, ISBN, genero, editorial, fechaPublicacion, resumen, imagen, UsuarioPrestado, historialPrestamos)