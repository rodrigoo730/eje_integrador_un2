from ManejadorIntegrante import ManejadorIntegrante
from ManejadorProyecto import ManejadorProyecto

if __name__ == '__main__':
    manejadorI = ManejadorIntegrante()
    manejadorI.cargarIntegrante()
    manejadorP = ManejadorProyecto()
    manejadorP.cargarProyecto()
    manejadorP.calcularPuntaje(manejadorI)
    manejadorP.listarProyecto()


