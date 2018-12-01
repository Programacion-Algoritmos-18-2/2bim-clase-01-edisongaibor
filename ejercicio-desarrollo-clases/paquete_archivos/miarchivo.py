
import codecs

class MiArchivo:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/datos.csv", "r")

    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:
    def cerrararchivo(self):
        self.archivo.close()
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/resultados.csv", "a")

    def agregar_informacion(self, imp):
        self.archivo.write("Nombre:%s | Promedio: %.2f" % (imp.nombre(), imp.promedio())
