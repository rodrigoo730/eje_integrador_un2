
class Integrante:
    __idProyecto=''
    __apellidoNombre=''
    __dni=''
    __categoriaInvestigacion=''
    __rol=''

    def __init__(self,id=0,AyN='',dni=0,categoria='',rol=''):
        self.__idProyecto = id
        self.__apellidoNombre = AyN
        self.__dni = dni
        self.__categoriaInvestigacion = categoria
        self.__rol = rol

    def getID(self):
        return self.__idProyecto

    def getRol(self):
        return self.__rol

    def getCategoria(self):
        return self.__categoriaInvestigacion





