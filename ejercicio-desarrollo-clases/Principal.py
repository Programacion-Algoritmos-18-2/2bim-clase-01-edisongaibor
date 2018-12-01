from paquete_archivo.datos import *
from paquete_modelo.modelo import *
 a = MiArchivo()
 a2 = MiArchivoEscribir()

lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

lista = lista[1:]

for d in lista:
    p = Persona(d[0],d[1], d[2], d[3])
    add2.agregardatos(p)
    print(p)
add.cerrar_archivo()
add2.cerrar_archivo()