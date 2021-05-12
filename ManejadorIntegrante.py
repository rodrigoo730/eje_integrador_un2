from IntegranteProyecto import Integrante
import csv
class ManejadorIntegrante:
    __lista = []

    def __init__(self):
        self.__lista = []

    def cargarIntegrante(self):
        archivo = open('integrantesProyecto.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = False
        for fila in reader:
            if not bandera:
                bandera = True
            else:
                integrante = Integrante(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__lista.append(integrante)
        archivo.close()

    def getLista(self):
        return self.__lista

    def getIdL(self,i):
        return self.__lista[i].getID()
    def getIntegrante(self,i):
        return self.__lista[i]