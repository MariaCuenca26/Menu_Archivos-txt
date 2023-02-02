from abc import ABC, abstractclassmethod

class Datos(ABC):
    
    @abstractclassmethod
    def mostrarDatos(self):
        pass