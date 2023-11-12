import sqlite3
from accionesLibro import AccionesAdministrador

class TomarLibrosDisponibles:
    resultados = AccionesAdministrador.verLibrosDisponibles()
    for i in resultados:
        print(i)    