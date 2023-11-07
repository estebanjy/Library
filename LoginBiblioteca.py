import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QMessageBox, QLineEdit, QPushButton, QCheckBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Registro import CrearNuevoUsuario


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
        # Etiqueta de ingreso a la aplicación
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
        """
        Cuando el usuario hace clic en el botón para registrarse, verifica si el nombre
        de usuario y la contraseña ya estan guardados en users.txt
        Si existe, muestra un mensaje y se cierra el programa
        Si no existe, muestra un mensaje de error
        """
        usuarios = {}  
        
        try:
            with open("archivos/users.txt", 'r') as f:
                for line in f:
                    campos_usuario = line.split(" ")
                    nombre_usuario = campos_usuario[0]
                    password = campos_usuario[1].strip('\n')
                    usuarios[nombre_usuario] = password
        except FileNotFoundError:
            print("El archivo no existe. Creando nuevo archivo de usuarios")
            f = open ("archivos/users.txt", "w")
            
        nombre_usuario = self.nombre_entrada.text()
        password = self.passwd_entrada.text()
        if (nombre_usuario, password) in usuarios.items():
            QMessageBox.information(self, "Inicio de sesión exitoso", "Inicio de sesión exitoso", QMessageBox.Ok, QMessageBox.Ok)
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
        self.create_new_user_dialog = CrearNuevoUsuario()  # importa el modulo de Registro
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


# Ejecuta el programa
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginUI()
    sys.exit(app.exec_())
