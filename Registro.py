"""
v.0.4
"""

import sys
from usuario import Administrador, UsuarioNormal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CrearNuevoUsuario(QWidget):
    def __init__(self):
        super().__init__()
        self.genero_seleccionado = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Registro de Usuario')
        self.setGeometry(300, 300, 400, 300)

        layout = QFormLayout()

        # Widget para mostrar icono de Nuevo Usuario
        icono_nuevo_usuario = "imagenes/nuevo_usuario.png"        
        self.nuevo_usuario = QLabel(self)
        self.nuevo_usuario.setAlignment(Qt.AlignCenter)
        self.nuevo_usuario.setFixedSize(100, 100)
        pixmap = QPixmap(icono_nuevo_usuario)
        self.nuevo_usuario.setPixmap(pixmap)

        # Widgets de campos de datos del usuario
        self.usuario_edit = QLineEdit(self)
        self.documento_edit = QLineEdit(self)
        self.telefono_edit = QLineEdit(self)
        self.domicilio_edit = QLineEdit(self)
        self.fecha_nacimiento_edit = QDateEdit(self)
        self.fecha_nacimiento_edit.setDisplayFormat("dd/MM/yyyy")        
        self.genero_radio_masculino = QRadioButton('Masculino')
        self.genero_radio_femenino = QRadioButton('Femenino')
        self.genero_radio_otros = QRadioButton('Otros')
        self.administrador_checkbox = QCheckBox('Administrador')
        self.contrasena_edit = QLineEdit()
        self.contrasena_edit.setEchoMode(QLineEdit.Password)
        self.confirmar_contrasena_edit = QLineEdit()
        self.confirmar_contrasena_edit.setEchoMode(QLineEdit.Password)
        self.confirmar_contrasena_edit.setPlaceholderText('Confirmar Contraseña')
        self.contrasena_admin_edit = QLineEdit()
        self.contrasena_admin_edit.setEchoMode(QLineEdit.Password)
        self.contrasena_admin_edit.setEnabled(False)
        self.confirmar_contrasena_admin_edit = QLineEdit()
        self.confirmar_contrasena_admin_edit.setEchoMode(QLineEdit.Password)
        self.confirmar_contrasena_admin_edit.setPlaceholderText('Confirmar Contraseña')
        self.confirmar_contrasena_admin_edit.setEnabled(False)

        self.genero_group = [self.genero_radio_masculino, self.genero_radio_femenino, self.genero_radio_otros]
        self.genero_radio_masculino.setChecked(True)

        layout.addRow(self.nuevo_usuario)
        layout.addRow('Nombre de Usuario:', self.usuario_edit)
        layout.addRow('Documento / DNI:', self.documento_edit)
        layout.addRow('Número de Teléfono:', self.telefono_edit)
        layout.addRow('Domicilio:', self.domicilio_edit)
        layout.addRow('Fecha de Nacimiento:', self.fecha_nacimiento_edit)

        # Radio Buttons (horizontales)para la etiqueta género
        genero_layout = QHBoxLayout()
        genero_layout.addWidget(self.genero_radio_masculino)
        genero_layout.addWidget(self.genero_radio_femenino)
        genero_layout.addWidget(self.genero_radio_otros)
        layout.addRow('Género:', genero_layout)
        # Conectar los radio buttons a la función correspondiente
        self.genero_radio_masculino.clicked.connect(self.on_radio_button_clicked)
        self.genero_radio_femenino.clicked.connect(self.on_radio_button_clicked)
        self.genero_radio_otros.clicked.connect(self.on_radio_button_clicked)

        # Contraseña de usuario
        layout.addRow('Contraseña usuario:', self.contrasena_edit)
        layout.addRow('', self.confirmar_contrasena_edit)

        # Contraseña de administrador
        layout.addRow('Tipo de usuario:', self.administrador_checkbox)
        layout.addRow('Contraseña admin:', self.contrasena_admin_edit)
        layout.addRow('', self.confirmar_contrasena_admin_edit)
        self.administrador_checkbox.clicked.connect(self.on_administrador_checkbox_clicked)

        # Boton de registro
        boton_registro = QPushButton("Registrarse", self)
        boton_registro.clicked.connect(self.registrarUsuario)
        layout.addRow('', boton_registro)
        
        self.setLayout(layout)

    def on_administrador_checkbox_clicked(self):
        self.contrasena_admin_edit.setEnabled(self.administrador_checkbox.isChecked())
        self.confirmar_contrasena_admin_edit.setEnabled(self.administrador_checkbox.isChecked())

    def on_radio_button_clicked(self):
        # Determinar qué radio button fue seleccionado
        if self.genero_radio_masculino.isChecked():
            self.genero_seleccionado = 'Masculino'
        elif self.genero_radio_femenino.isChecked():
            self.genero_seleccionado = 'Femenino'
        elif self.genero_radio_otros.isChecked():
            self.genero_seleccionado = 'Otros'

    def registrarUsuario(self):
        """
        Cuando el usuario clickea en Reguistrarse, verifica que las contraseñas coincidan
        si coinciden, se guarda en nombre de usuario y contraseña en el archivo users.txt
        """
        contrasena = self.contrasena_edit.text()
        confirmar_password = self.confirmar_contrasena_edit.text()
        if contrasena != confirmar_password:
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden. Inténtelo de nuevo.", QMessageBox.Close, QMessageBox.Close)
        else:
            if self.administrador_checkbox.isChecked():
                if self.contrasena_admin_edit.text() != "Luis Miguel": 
                    QMessageBox.warning(self, "Error", "No es la Contraseña correcta. Inténtelo de nuevo.", QMessageBox.Close, QMessageBox.Close)
                else: 
                    Administrador(self.usuario_edit.text(), self.documento_edit.text(), self.telefono_edit.text(), self.domicilio_edit.text(), self.fecha_nacimiento_edit.text(), self.genero_seleccionado, contrasena).generarAdministrador()

                    self.close()
                    QMessageBox.information(self, 'Registro Exitoso', 'Administrador registrado exitosamente!')
            else: 
                UsuarioNormal(self.usuario_edit.text(), self.documento_edit.text(), self.telefono_edit.text(), self.domicilio_edit.text(), self.fecha_nacimiento_edit.text(), self.genero_seleccionado, contrasena).generarUsuarioNomal()

                self.close()
                QMessageBox.information(self, 'Registro Exitoso', 'Usuario registrado exitosamente!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CrearNuevoUsuario()
    ex.show()
    sys.exit(app.exec_())