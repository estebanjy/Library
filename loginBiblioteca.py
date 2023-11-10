import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QMessageBox, QLineEdit, QPushButton, QCheckBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Registro import CrearNuevoUsuario    
import sqlite3
from hash import Hash
from datosUsuarios import datosUsuario

class LoginUI(QWidget):

    def __init__(self):  # Constructor
        super().__init__()
        self.inicializarUI()
    
    def inicializarUI(self):
        self.setGeometry(100, 100, 420, 240)
        self.setWindowTitle('Login')
        self.interfazLogin()
        self.show()
    
    def interfazLogin(self):
        etiqueta_login = QLabel(self)
        etiqueta_login.setText("Ingresar a la Biblioteca")
        etiqueta_login.move(80, 10)
        etiqueta_login.setFont(QFont('Arial', 20))
        
        # Widgets de nombre de usuario y contraseña
        etiqueta_nombre = QLabel("Nombre de usuario:", self)
        etiqueta_nombre.move(35, 60)
        self.nombre_entrada = QLineEdit(self)
        self.nombre_entrada.move(165, 60)
        self.nombre_entrada.resize(220, 20)
        etiqueta_passwd = QLabel("Contraseña:", self)
        etiqueta_passwd.move(35, 90)
        self.passwd_entrada = QLineEdit(self)
        self.passwd_entrada.move(165, 90)
        self.passwd_entrada.resize(220, 20)

        # Botón de acceso
        boton_acceso = QPushButton('Acceder', self)
        boton_acceso.move(110, 145)
        boton_acceso.resize(200, 40)
        boton_acceso.clicked.connect(self.clickLoguearse)
        
        # Checkbox para mostrar contraseña
        mostrar_contraseña = QCheckBox("Mostrar contraseña", self)
        mostrar_contraseña.move(163, 115)
        mostrar_contraseña.stateChanged.connect(self.mostrarPasswd)
        mostrar_contraseña.toggle()
        mostrar_contraseña.setChecked(False)
        
        # Botón para registrarse
        nuevo_socio = QLabel("¿No sos socio?", self)
        nuevo_socio.move(70, 203)
        registrarse = QPushButton("Registrarse", self)
        registrarse.move(170, 195)
        registrarse.clicked.connect(self.crearNuevoUsuario)
    
    def clickLoguearse(self):
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        """
        Cuando el usuario hace clic en el botón para registrarse, verifica si el nombre
        de usuario y la contraseña ya estan guardados en usersrama.txt
        Si existe, muestra un mensaje y se cierra el prog
        Si no existe, muestra un mensaje de error
        """     
        nombre = self.nombre_entrada.text()
        contrasenia = self.passwd_entrada.text()

        user = cursor.execute("""SELECT Nombre, Contrasenia, IDUsuarioNormal FROM Usuarios
        WHERE Nombre = ?""", (nombre, ))

        admin = cursor.execute("""SELECT Nombre, Contrasenia FROM Administradores
        WHERE Nombre = ?""", (nombre, ))
        
        bandera = False
        EsAdmin = False 
        
        
        resultado = admin.fetchall()
        for i in resultado:
            if Hash.check_password(i[1], contrasenia):
                bandera = True
                EsAdmin = True
                break 
        
        resultado = user.fetchall() 
        for i in resultado:
            if Hash.check_password(i[1], contrasenia()):
                bandera = True 
                resultado = i[3] 
                break

        if bandera:
            QMessageBox.information(self, "Inicio de sesión exitoso", "Inicio de sesión exitoso", QMessageBox.Ok, QMessageBox.Ok)
            
            if EsAdmin:
                self.close()
                #aqui hay que enlazarlo con el menu principal
            else:
                id = datosUsuario(resultado)
                #aqui hay que retornar el id del usuario normal ya que sera necesario en otras funciones
                self.close()
        else:
            QMessageBox.warning(self, "Error", "El nombre de usuario o la contraseña son incorrectos", QMessageBox.Close, QMessageBox.Close)
            
    def mostrarPasswd(self, state):
        if state == Qt.Checked:
            self.passwd_entrada.setEchoMode(QLineEdit.Normal)
        else:
            self.passwd_entrada.setEchoMode(QLineEdit.Password)
    
    def crearNuevoUsuario(self):
        """
        Cuando se hace clic en este botón, se abre una nueva ventana
        para crear una cuenta nueva
        """
        self.create_new_user_dialog = CrearNuevoUsuario()  # importa el modulo de registro
        self.create_new_user_dialog.show()
    
    def eventoCerrar(self, event):
        """
        Muestra un mensaje preguntanfo si desea salir de la aplicación
        """
        mensaje_salida = QMessageBox.question(self, "¿Salir de la aplicación?", "¿Está seguro que desea salir?", QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if mensaje_salida == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginUI()
    sys.exit(app.exec_())