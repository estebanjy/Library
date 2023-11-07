import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox, QPushButton, QLabel, QLineEdit)
from PyQt5.QtGui import QFont, QPixmap


class CrearNuevoUsuario(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        # Inicializa la ventana y muestra su contenido a la pantalla
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Registrar nuevo usuario')
        self.RecopilarInformacion()
        self.show()

    def RecopilarInformacion(self):
        """
        Crea los widgets para recopilar información para crear una nueva cuenta
        Etiqueta de Nuevo Usuario
        """
        icono_nuevo_usuario = "imagenes/nuevo_usuario.png"
        try:
            with open(icono_nuevo_usuario):
                nuevo_usuario = QLabel(self)
                pixmap = QPixmap(icono_nuevo_usuario)
                nuevo_usuario.setPixmap(pixmap)
                nuevo_usuario.move(150, 60)
        except FileNotFoundError:
            print("No se encontró la imagen.")
        
        etiqueta_login = QLabel(self)
        etiqueta_login.setText("Nueva cuenta")
        etiqueta_login.move(120, 15)
        etiqueta_login.setFont(QFont('Arial', 20))
        
        # Etiquetas de nombre de usuario y nombre completo
        etiqueta_login = QLabel("Nombre de usuario:", self)
        etiqueta_login.move(35, 180)
        self.nombre = QLineEdit(self)
        self.nombre.move(165, 180)
        self.nombre.resize(200, 20)
        etiqueta_login = QLabel("Nombre completo:", self)
        etiqueta_login.move(35, 210)
        nombre = QLineEdit(self)
        nombre.move(165, 210)
        nombre.resize(200, 20)
        
        # Crea etiquetas de contraseña y confirmación de contraseña
        etiqueta_passwd = QLabel("Contraseña:", self)
        etiqueta_passwd.move(35, 240)
        self.passwd = QLineEdit(self)
        self.passwd.setEchoMode(QLineEdit.Password)
        self.passwd.move(165, 240)
        self.passwd.resize(200, 20)
        etiqueta_confirmar = QLabel("Confirmar:", self)
        etiqueta_confirmar.move(35, 270)
        self.confirmar_entrada = QLineEdit(self)
        self.confirmar_entrada.setEchoMode(QLineEdit.Password)
        self.confirmar_entrada.move(165, 270)
        self.confirmar_entrada.resize(200, 20)
        
        # botón de registro
        boton_registro = QPushButton("Registrarse", self)
        boton_registro.move(100, 310)
        boton_registro.resize(200, 40)
        boton_registro.clicked.connect(self.confirmarRegistro)

    def confirmarRegistro(self):
        """
        Cuando el usuario clickea en Reguistrarse, verifica que las contraseñas coincidan
        si coinciden, se guarda en nombre de usuario y contraseña en el archivo users.txt
        """
        texto_passwd = self.passwd.text()
        confirmar_texto = self.confirmar_entrada.text()
        if texto_passwd != confirmar_texto:
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden. Inténtelo de nuevo.", QMessageBox.Close, QMessageBox.Close)
        else:
            with open("archivos/users.txt", 'a+') as f:
                f.write(self.nombre.text() + " ")
                f.write(texto_passwd + "\n")
            self.close()


# Ejecuta el programa
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CrearNuevoUsuario()
    sys.exit(app.exec_())
