from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QDialog,QFormLayout, QWidget, QLabel, QPushButton, QVBoxLayout,  QComboBox, QLineEdit,QHBoxLayout,QStackedWidget
from PyQt5.QtGui import QPixmap
from accionesLibro import Acciones
import sys

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        #self.contadorPagina = 0

        """accion = Acciones()
        libros = accion.verLibrosDisponibles()
        layout = QFormLayout()

        self.titulo = QLabel(self)
        self.editorial = QLabel(self)
        self.resumen = QLabel(self)
        self.anio = QLabel(self)

        self.titulo.setText(f"Titulo: {libros[self.contadorPagina][1]}")
        self.editorial.setText(f"Editorial: {libros[self.contadorPagina][1]}")
        self.resumen.setText(f"Resumen: {libros[self.contadorPagina][1]}")
        self.anio.setText(f"Año de publicacion: {libros[self.contadorPagina][1]}")"""

        """datosLayout = QVBoxLayout(self)
        datosLayout.addLayout(self.titulo)
        datosLayout.addLayout(self.editorial)
        datosLayout.addLayout(self.resumen)
        datosLayout.addLayout(self.anio)"""

        #CREAR BOTON DE FILTRAR BUSQUEDA
        self.Bt_Filtro = QPushButton('Filtrar', self)
        self.Bt_Filtro.clicked.connect(self.FiltrarBusqueda)
        self.Bt_Filtro.setFixedWidth(80)

        #Opciones desplegable de genero
        self.genero_combobox = QComboBox(self)
        self.genero_combobox.addItem('Todos los Géneros')
        self.genero_combobox.addItem('Ficción')
        self.genero_combobox.addItem('No Ficción')
        self.genero_combobox.addItem('Misterio')
        self.genero_combobox.setFixedWidth(150)  # Ancho FIJO

        #Opciones desplegable de categoria
        self.categoria_combobox = QComboBox(self)
        self.categoria_combobox.addItem('Todas las Categorías')
        self.categoria_combobox.addItem('Novela')
        self.categoria_combobox.addItem('Historia')
        self.categoria_combobox.addItem('Ciencia')
        self.categoria_combobox.setFixedWidth(150)

        #buscador
        self.BarraBuscador = QLineEdit(self)
        textoBarra = self.BarraBuscador.text()
        self.Bt_Buscador = QPushButton('Buscar', self)
        self.Bt_Buscador.clicked.connect(lambda: self.realizar_busqueda(textoBarra))

        #LabelLibro
        self.labelImg = QLabel(self)
        self.labelImg.setFixedSize(200, 200)
        self.labelImg.setStyleSheet('background-color: black')
        #self.labelImg.mousePressEvent = self.mostrar_informacion_imagen
        #diseño horizontal para el botón de filtrar
        Filtro_layout = QHBoxLayout()
        Filtro_layout.addWidget(self.Bt_Filtro)
        Filtro_layout.addWidget(self.genero_combobox)
        Filtro_layout.addWidget(self.categoria_combobox)

        #diseño horizontal para el buscador
        Buscador_layout = QHBoxLayout()
        Buscador_layout.addWidget(self.BarraBuscador)
        Buscador_layout.addWidget(self.Bt_Buscador)

        Labelhbox = QHBoxLayout()
        Labelhbox.addWidget(self.labelImg)
        #Labelhbox.addWidget(datosLayout)


        Bt_Anterior = QPushButton('Anterior', self)
        Bt_Siguiente = QPushButton('Siguiente', self)
        self.label_num_pagina = QLabel('Página 1', self)

        Bt_Anterior.clicked.connect(lambda: self.cambiar_pagina(-1))
        Bt_Siguiente.clicked.connect(lambda: self.cambiar_pagina(1))

        # diseño horizontal para los botones y el label
        inferior_layout = QHBoxLayout()
        inferior_layout.addWidget(Bt_Anterior)
        inferior_layout.addWidget(self.label_num_pagina)
        inferior_layout.addWidget(Bt_Siguiente)

        main_layout = QVBoxLayout(self)
        main_layout.addLayout(Buscador_layout)
        main_layout.addLayout(Filtro_layout)
        main_layout.addLayout(Labelhbox)
        main_layout.addLayout(inferior_layout)

        self.contadorPagina = 0


    def FiltrarBusqueda(self):
        textCategoria = self.categoria_combobox.currentText()
        textGenero = self.genero_combobox.currentText()
    def realizar_busqueda(self,text):

        accion = Acciones()
        libros = accion.busquedaLibro(text)
        imagen = libros[0]
        pixmap = QPixmap(imagen)
        self.labelImg.setPixmap(pixmap)


        #for i in libros():
            #if i[1] == text:
                #imagen = self.libros[i][0]
                #pixmap = QPixmap(imagen)
                #self.labelImg.setPixmap(pixmap)
            #else:
                #self.labelImg.setText("No se encuentra el libro")
        pass


    def cambiar_pagina(self, valor):
        # Cambiar la página actual en función de la dirección
        self.contadorPagina += valor
        self.contadorPagina = max(0, min(self.contadorPagina, 3))
        self.actualizar_pagina()

    def actualizar_pagina(self):
        self.label_num_pagina.setText(f'Página {self.contadorPagina + 1}')
        #self.mostrar_imagenes_actuales()

    def mostrar_imagenes_actuales(self):
        imagen = self.libros[self.contadorPagina][0]
        pixmap = QPixmap(imagen)
        self.labelImg.setPixmap(pixmap)

    #def mostrar_informacion_imagen(self):
        #ventanaLibro = newVentana()
        #ventanaLibro.exec_()

"""class newVentana(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pedir Libro")
        self.setGeometry(200, 200, 200, 150)

        layout = QVBoxLayout()
        self.setLayout(layout)"""



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())


