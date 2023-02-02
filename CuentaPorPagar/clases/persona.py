from abc import ABC, abstractmethod 

class Persona(ABC):
    """docstring for Persona."""
    _secuencia = 0
    def __init__(self, nombre:str, estado:bool, id:int= 0):
        Persona._secuencia += 1
        self.__id = id if id > 0 else Persona._secuencia 
        self.nombre = nombre
        self.estado = estado
        super(Persona, self).__init__()
        
    @property
    def codigo(self):
        return self.__id
    
    @abstractmethod
    def mostarDatos(self):
        pass