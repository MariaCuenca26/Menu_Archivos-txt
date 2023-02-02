from clases.datos import Datos

class DetalleDeuda(Datos):
    """docstring for Compra."""
    _secuencia = 0
    def __init__(self, aamm:str, cuota:float, estado:bool=False, id:int=0):
        DetalleDeuda._secuencia += 1 
        self.__id = id if id>0 else DetalleDeuda._secuencia 
        self.aamm = aamm
        self.cuota = cuota
        self.estado = estado
        
    def mostrarDatos(self):
        print(self.codigo, self.aamm, self.cuota, self.estado)
    
    @property
    def codigo(self):
        return self.__id
    
    def getDetalleDeuda(self):
        return [str(self.codigo), str(self.cuota) , self.aamm, str(self.estado)]
    
if __name__ == '__main__':
    d = DetalleDeuda('929', 12)
    print(d.mostrarDatos())
    