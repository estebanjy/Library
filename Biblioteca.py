import sqlite3

class Biblioteca:
    def __init__(self):
        pass
    
    def crearBaseDatos():
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS Administradores(
            Nombre TEXT,
            Dni INTEGER,
            Telefono INTEGER,
            Domicilio TEXT,
            FechaNacimiento TEXT,
            Sexo TEXT,
            Contrasenia TEXT,
            IDAdministrador TEXT PRIMARY KEY
            );""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS Usuarios( 
            Nombre TEXT,
            Dni INTEGER,
            Telefono INTEGER,
            Domicilio TEXT,
            FechaNacimiento TEXT,
            Sexo TEXT,
            Contrasenia TEXT,
            IDUsuarioNormal TEXT PRIMARY KEY
            );""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS Libros(
            Titulo TEXT,
            Autores TEXT,
            ISBN TEXT PRIMARY KEY, 
            Genero TEXT,
            Editorial TEXT,
            FechaPublicacion TEXT,
            Resumen TEXT,
            Imagen TEXt,
            IDUsuarioNormal TEXT, 
            HistorialPrestamos TEXT,
            FOREIGN KEY(IDUsuarioNormal) REFERENCES Usuarios
            );""")
        conexion.commit() 
        cursor.close()
        conexion.close()      
    
    
s = Biblioteca()
Biblioteca.crearBaseDatos()