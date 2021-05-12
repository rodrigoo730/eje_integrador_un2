import csv
from Proyecto import Proyecto
from IntegranteProyecto import Integrante
class ManejadorProyecto:
    __lista =[]

    def __init__(self):
        self.__lista = []

    def cargarProyecto(self):
        archivo = open('proyectos.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = False
        for fila in reader:
            if not bandera:
                bandera = True
            else:
                proyecto = Proyecto(fila[0],fila[1],fila[2])
                self.__lista.append(proyecto)
        archivo.close()

    def listarProyecto(self):
        self.__lista.sort()                                                         #ordena la lista sobrecargando el operador
        print('Listado de proyectos:')
        for i in range(len(self.__lista)):
            print('Id:{}    titulo:{}    palabras Claves:{}    puntaje:{}'.format(self.__lista[i].getId(),self.__lista[i].getTitulo(),self.__lista[i].getPC(),self.__lista[i].getPuntaje()))

    def calcularPuntaje(self,MI):
        for k in range(len(self.__lista)):                                      # para cada proyecto
            listaI = []
            for j in range(len(MI.getLista())):                                 #recorro los integrantes y guardo en una lista los integrantes de un proyecto
                if self.__lista[k].getId() == MI.getIdL(j):
                    listaI.append(MI.getIntegrante(j))
            cont = 0
            puntaje = 0
            bandera_d = False
            bandera_c = False
            print('Mensajes de las reglas del proyecto: '.format(k + 1))
            for i in range(len(listaI)):                                        #recorro la lista de integrantes y calculo el puntaje
                if listaI[i].getRol() == 'director':
                    bandera_d = True
                    if listaI[i].getCategoria() in ['I','II']:                      #si director cumple con la categoria
                        puntaje += 10
                    else:
                        print('El Director del Proyecto debe tener categoría I o II')
                        puntaje -= 5
                elif listaI[i].getRol() == 'codirector':
                    bandera_c= True
                    if listaI[i].getCategoria() in ['I', 'II', 'III']:                  #si codirector cumple con la categoria
                        puntaje += 10
                    else:
                        print('El Codirector del Proyecto debe tener como mínimo categoría III’')
                        puntaje -= 5
                elif listaI[i].getRol() == 'integrante':
                    cont += 1

            if cont >= 3:                                                                                           #si tiene menos de 3 integrantes
                puntaje += 10
            else:
                print('El Proyecto debe tener como mínimo 3 integrantes')
                puntaje -= 20
            if not bandera_d:                                                                                       #sino tiene director
                print('El Proyecto debe tener un Director')
            if not bandera_c:                                                                                       #sino tiene codictor
                print('El Proyecto debe tener un codirector')
            if not bandera_c or not bandera_d:                                                                      #sino tiene director o codirector
                puntaje -= 10
            self.__lista[k].setPuntaje(puntaje)                                                                     #guardo el puntaje en el proyecto
            print('\n')


