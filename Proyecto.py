
class Proyecto:
    __idProyecto=''
    __titulo=''
    __palabraClave=''
    __puntaje=0

    def __init__(self,id=0,titulo='',palabraC='',puntaje=0):
        self.__idProyecto = id
        self.__titulo = titulo
        self.__palabraClave = palabraC
        self.__puntaje = puntaje

    def getId(self):
        return self.__idProyecto

    def getTitulo(self):
        return self.__titulo
    def getPC(self):
        return self.__palabraClave
    def getPuntaje(self):
        return self.__puntaje

    def setPuntaje(self,puntaje):
        self.__puntaje += puntaje


    def __gt__(self, other):
        if type(other) == Proyecto:
            return self.__puntaje < other.getPuntaje()
        else:
            print('Error de tipó de dato')

