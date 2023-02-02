from clases.proveedor import Proveedor

class Compra:
    """docstring for Compra."""
    _secuencia = 0
    def __init__(self, proveedor:Proveedor, fecha_compra:str, valorTotal:float, estado:bool=True, id:int=0):
        Compra._secuencia += 1 
        self.__id = self.__id = id if id > 0 else Compra._secuencia 
        self.proveedor = proveedor
        self.fecha_compra = fecha_compra
        self.valorTotal = valorTotal
        self.estado = estado
        
    def mostarDatos(self):
        print(self.codigo, self.proveedor.nombre, self.fecha_compra, self.valorTotal, self.estado)
    
    @property
    def codigo(self):
        return self.__id
    
    def getCompra(self):
        return [str(self.codigo), str(self.proveedor.codigo), self.fecha_compra, str(self.valorTotal), str(self.estado)]