from  generarID import GenerarIDAdministrador, GenerarIDUsuario 
from hash import Hash
from abc import ABC,abstractclassmethod
import sqlite3
from accionesLibro import AccionesUsuarioNormal
from libro import Libro

class Usuario(ABC):
    @abstractclassmethod
    def __init__(self, nombre, dni, telefono, domicilio, fechaNacimiento, sexo, contrasenia):
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono
        self.domicilio = domicilio
        self.fechaNacimiento = fechaNacimiento
        self.sexo = sexo
        self.contrasenia = Hash.hash_password(contrasenia) 

class Administrador(Usuario):
    def __init__(self, nombre, dni, telefono, domicilio, fechaNacimiento, sexo,contrasenia):
        super().__init__(nombre, dni, telefono, domicilio, fechaNacimiento, sexo, contrasenia)
        self.IDAdministrador = GenerarIDAdministrador(nombre, dni).generarID()
    
    def generarAdministrador(self):
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        cursor.execute("""INSERT INTO Administradores(Nombre, Dni, Telefono, Domicilio, FechaNacimiento, Sexo, Contrasenia, IDAdministrador) 
        VALUES (? , ?, ?, ?, ?, ?, ?, ?)
        """,(self.nombre, self.dni, self.telefono, self.domicilio, self.fechaNacimiento, self.sexo, self.contrasenia, self.IDAdministrador))
        conexion.commit()
        cursor.close()
        conexion.close()
    
class UsuarioNormal(Usuario):
    def __init__(self, nombre, dni, telefono, domicilio, fechaNacimiento, sexo, contrasenia):
        super().__init__(nombre, dni, telefono, domicilio, fechaNacimiento, sexo, contrasenia)
        self.IDUsuarioNormal = GenerarIDUsuario(nombre, dni).generarID()
    
    def generarUsuarioNomal(self): 
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        cursor.execute("""INSERT INTO Usuarios(Nombre, Dni, Telefono, Domicilio, FechaNacimiento, Sexo, Contrasenia, IDUsuarioNormal) 
        VALUES (? , ?, ?, ?, ?, ?, ?, ?)
        """,(self.nombre, self.dni, self.telefono, self.domicilio, self.fechaNacimiento, self.sexo, self.contrasenia, self.IDUsuarioNormal))
        conexion.commit()
        cursor.close()
        conexion.close()

#id = GenerarIDUsuario("aguilar", "131233").generarID()  

#l = Libro("el hobbit", "asd", "asdsad", "accion", "asdd", "asdasd", " aksdjsa", "asdlkj")
#s.generarAdministrador()
#AccionesUsuarioNormal.devolverLibro(l)