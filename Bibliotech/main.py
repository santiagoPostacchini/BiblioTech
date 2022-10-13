import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

# Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    # Método constructor de la clase
    def __init__(self):
        # Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        # Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("ui/BiblioTech.ui", self)
        self.setWindowTitle("BiblioTech")

# Instancia para iniciar una aplicación
app = QApplication(sys.argv)
# Crear un objeto de la clase
_ventana = Ventana()
# Mostra la ventana
_ventana.show()
# Ejecutar la aplicación
app.exec_()




# nuevoSocio_inicio
# nuevoLibro_inicio
# nuevoArticulo_inicio
# nuevoPrestamo_inicio

# nuevoSocio_socios
# buscarSocio_socios
# bucadorSocio_socios
# tablaSocios_socios
# tablaPrestamos_socios
# nombreSocio_socios
# dniSocio_socios
# apellidoSocio_socios
# emailSocio_socios
# tipoSocio_socios
# anioSocio_socios
# eliminarSocio_socios
# editarSocio_socios

# buscarItem_inventario
# buscadorItem_inventario
# tablaItems_inventario
# tituloLibro_inventario
# generoLibro_inventario
# ISBN_inventario
# editorialLibro_inventario
# autorLibro_inventario
# estadoLibro_inventario
# tipoLibro_inventario
# nuevoLibro_inventario
# imagenLibro_inventario
# nombreArticulo_inventario
# marcaArticulo_inventario
# tipoArticulo_inventario
# estadoArticulo_inventario
# imagenArticulo_inventario
# nuevoArticulo_inventario

# buscarPrestamo_prestamos
# buscadorPrestamo_prestamos
# nuevoPrestamo_prestamos
# tablaPrestamo_prestamos
# datosUsuario_prestamos
# listaItems_prestamos
# fechaCreacion_prestamos
# fechaDevolucion_prestamos
# barraVerticalListaItems_prestamos

# ordenCatalogo_catalogo
# filtroCatalogo_catalogo
# buscarCatalogo_catalogo
# buscadorCatalogo_catalogo
# barraVerticalCatalogo_catalogo
