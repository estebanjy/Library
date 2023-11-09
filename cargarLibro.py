"""
v.0.3
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

        # Widget para mostrar la imagen de la tapa del libro
        self.imagen_tapa_label = QLabel()
        self.imagen_tapa_label.setAlignment(Qt.AlignCenter)
        self.imagen_tapa_label.setFixedSize(70, 80)
        self.cargar_imagen_button = QPushButton('Cargar Tapa del Libro')
        self.cargar_imagen_button.clicked.connect(self.cargar_imagen)

        # 
        self.titulo_edit = QLineEdit(self)
        self.autores_edit = QLineEdit(self)
        self.isbn_edit = QLineEdit(self)
        self.genero_edit = QLineEdit(self)
        self.editorial_edit = QLineEdit(self)
        self.fecha_publicacion_edit = QDateEdit(self)
        self.fecha_publicacion_edit.setDisplayFormat("dd/MM/yyyy")
        self.resumen_edit = QTextEdit(self)

        layout.addRow('Tapa del Libro:', self.imagen_tapa_label)
        layout.addRow('', self.cargar_imagen_button)
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

    def cargar_imagen(self):
        # Abrir un cuadro de diálogo para seleccionar la imagen de la tapa del libro
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Archivos de Imagen (*.png *.jpg *.jpeg *.bmp)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]

            # Mostrar la imagen en el widget QLabel
            pixmap = QPixmap(file_path)
            self.imagen_tapa_label.setPixmap(pixmap)
            self.imagen_tapa_label.setScaledContents(True)

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

