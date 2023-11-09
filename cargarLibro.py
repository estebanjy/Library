"""
v.0.2
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CargarLibro(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Cargar Nuevo Libro')
        self.setGeometry(300, 300, 400, 300)

        layout = QFormLayout()

        self.titulo_edit = QLineEdit(self)
        self.autores_edit = QLineEdit(self)
        self.isbn_edit = QLineEdit(self)
        self.genero_edit = QLineEdit(self)
        self.editorial_edit = QLineEdit(self)
        self.fecha_publicacion_edit = QDateEdit(self)
        self.fecha_publicacion_edit.setDisplayFormat("dd/MM/yyyy")
        self.resumen_edit = QTextEdit(self)

        layout.addRow('Título:', self.titulo_edit)
        layout.addRow('Autor/es:', self.autores_edit)
        layout.addRow('ISBN:', self.isbn_edit)
        layout.addRow('Género:', self.genero_edit)
        layout.addRow('Editorial:', self.editorial_edit)
        layout.addRow('Fecha de Publicación:', self.fecha_publicacion_edit)
        layout.addRow('Resumen:', self.resumen_edit)

        registro_button = QPushButton('Cargar libro')
        registro_button.clicked.connect(self.registrar_libro)

        layout.addRow('', registro_button)

        self.setLayout(layout)

    def registrar_libro(self):
        with open("archivos/libros.txt", 'a+') as f:
            f.write(self.titulo_edit.text() + " ")
            f.write(self.autores_edit.text() + " ")
            f.write(self.isbn_edit.text() + " ")
            f.write(self.editorial_edit.text() + " ")
            f.write(self.fecha_publicacion_edit.text() + " ")
            f.write(self.resumen_edit.text() + "\n")
        self.close()
        QMessageBox.information(self, 'Registro Exitoso', 'Libro registrado exitosamente!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CargarLibro()
    ex.show()
    sys.exit(app.exec_())
