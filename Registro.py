import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox, QButtonGroup, QPushButton, QLabel, QLineEdit)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.Qt import QRadioButton


class CrearNuevoUsuario(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        # Inicializa la ventana y muestra su contenido a la pantalla
        self.setGeometry(100, 100, 400, 500)
        self.setWindowTitle('Registrar nuevo usuario')
        self.recopilarInformacion()
        self.show()

    def recopilarInformacion(self):
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
        
        # Etiquetas de nombre de usuario
        etiqueta_nombre = QLabel("Nombre de usuario:", self)
        etiqueta_nombre.move(35, 180)
        self.nombre = QLineEdit(self)
        self.nombre.move(165, 180)
        self.nombre.resize(200, 20)
        
        # Etiqueta documento
        etiqueta_dni = QLabel("Documento/DNI:", self)
        etiqueta_dni.move(35, 210)
        self.dni = QLineEdit(self)
        self.dni.move(165, 210)
        self.dni.resize(200, 20)
        
        # Etiqueta nro.de telefono
        etiqueta_tel = QLabel("Teléfono/Cel.:", self)
        etiqueta_tel.move(35, 240)
        self.tel = QLineEdit(self)
        self.tel.move(165, 240)
        self.tel.resize(200, 20)
        
        # Etiqueta domicilio
        etiqueta_domicilio = QLabel("Domicilio:", self)
        etiqueta_domicilio.move(35, 270)
        self.domicilio = QLineEdit(self)
        self.domicilio.move(165, 270)
        self.domicilio.resize(200, 20)
        
        # Etiqueta fecha de nacimiento
        etiqueta_fecha_nac = QLabel("Fecha de Nac.:", self)
        etiqueta_fecha_nac.move(35, 300)
        self.nacimiento = QLineEdit(self)
        self.nacimiento.move(165, 300)
        self.nacimiento.resize(200, 20)
               
        # Etiqueta sexo y radioButtons
        etiqueta_sexo = QLabel("Sexo:", self)
        etiqueta_sexo.move(35, 330)
        rb_masculino = QRadioButton("masculino", self)
        rb_masculino.move(100, 330)
        rb_femenino = QRadioButton("femenino", self)
        rb_femenino.move(210, 330)
        rb_otro = QRadioButton("otro", self)
        rb_otro.move(314, 330)
        rb_grupo = QButtonGroup(self)
        rb_grupo.addButton(rb_masculino)
        rb_grupo.addButton(rb_femenino)
        rb_grupo.addButton(rb_otro)
                
        # Crea etiquetas de contraseña y confirmación de contraseña
        etiqueta_passwd = QLabel("Contraseña:", self)
        etiqueta_passwd.move(35, 360)
        self.passwd = QLineEdit(self)
        self.passwd.setEchoMode(QLineEdit.Password)
        self.passwd.move(165, 360)
        self.passwd.resize(200, 20)
        etiqueta_confirmar = QLabel("Confirmar:", self)
        etiqueta_confirmar.move(35, 390)
        self.confirmar_entrada = QLineEdit(self)
        self.confirmar_entrada.setEchoMode(QLineEdit.Password)
        self.confirmar_entrada.move(165, 390)
        self.confirmar_entrada.resize(200, 20)
        
        # botón de registro
        boton_registro = QPushButton("Registrarse", self)
        boton_registro.move(100, 430)
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
