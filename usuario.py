from  generarID import GenerarIDAdministrador, GenerarIDUsuario 
from abc import ABC,abstractclassmethod
import sqlite3

class Usuario(ABC):
    @abstractclassmethod
    def __init__(self, nombre, dni, telefono, domicilio, fechaNacimiento, sexo, contrasenia):
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono
        self.domicilio = domicilio
        self.fechaNacimiento = fechaNacimiento
        self.sexo = sexo
        self.contrasenia = contrasenia

class Administrador(Usuario):
    def __init__(self, nombre, dni, telefono, domicilio, fechaNacimiento, sexo):
        super().__init__(nombre, dni, telefono, domicilio, fechaNacimiento, sexo)
        self.IDAdministrador = GenerarIDAdministrador(nombre, dni)
    
    def generarAdministrador(self):
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        cursor.execute("""INSERT INTO Administradores(Nombre, Dni, Telefono, Domicilio, FechaNacimiento, Sexo, Contrasenia, IDAdministrador) 
        VALUES ("()", (), (), "()", "()", "()", "()", "()")
        """) .format(self.nombre, self.dni, self.telefono, self.domicilio, self.fechaNacimiento, self.sexo, self.contrasenia, self.IDAdministrador)
        conexion.commit()
        cursor.close()
        conexion.close()
    
class UsuarioNormal(Usuario):
    def __init__(self, nombre, dni, telefono, domicilio, fechaNacimiento, sexo):
        super().__init__(nombre, dni, telefono, domicilio, fechaNacimiento, sexo)
        self.IDUsuarioNormal = GenerarIDUsuario(nombre, dni)
    
    def generarUsuarioNomal(self): 
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        cursor.execute("""INSERT INTO Administradores(Nombre, Dni, Telefono, Domicilio, FechaNacimiento, Sexo, Contrasenia, IDUsuarioNormal) 
        VALUES ("()", (), (), "()", "()", "()", "()", "()")
        """) .format(self.nombre, self.dni, self.telefono, self.domicilio, self.fechaNacimiento, self.sexo, self.contrasenia, self.IDUsuarioNormal)
        conexion.commit()
        cursor.close()
        conexion.close()