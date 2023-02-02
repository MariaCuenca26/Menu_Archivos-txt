
from clases.compra import Compra
from clases.detalleDeuda import DetalleDeuda


class Deuda:
    """docstring for Compra."""
    _secuencia = 0
    def __init__(self, compra:Compra, fecha_credito:str, valorCredito:float, NoCuotas:int, valorCuota:float, aammInitial:int, estado:bool=False, id=0):
        Deuda._secuencia += 1 
        self.__id = id if id>0 else Deuda._secuencia 
        self.compra = compra
        self.fecha_credito = fecha_credito
        self.valorCredito = valorCredito
        self.NoCuotas = NoCuotas
        self.valorCuota = valorCuota
        self.aammInitial = aammInitial
        self.detDeuda = []
        self.estado = estado
        
    def mostarDatos(self):
        print(self.codigo, self.fecha_credito, self.valorCredito, self.estado,  self.compra.fecha_compra, self.compra.proveedor.nombre)
    
    @property
    def codigo(self):
        return self.__id
        
    def agregarDetalleDeuda(self, fecha:str, cuota:int, estado:bool=False, id=0):
        detalle = DetalleDeuda(fecha, cuota, estado, id)
        self.detDeuda.append(detalle)
        
    def getDeuda(self):
        return [str(self.codigo), 
                str(self.compra.codigo), 
                self.fecha_credito,
                str(self.valorCredito),
                str(self.NoCuotas),
                str(self.valorCuota),
                self.aammInitial,
                str(self.estado)
                ]