from clases.persona import Persona

class Proveedor(Persona):
    """docstring for Proveedor."""
    def __init__(self, nombre:str, estado:bool, direccion:str, telefono:str, credito:bool, id:int=0):
        super(Proveedor, self).__init__(nombre, estado, id=id)
        self.direccion = direccion
        self.telefono = telefono
        self.credito = credito
    
    def mostarDatos(self):
        print(self.codigo, self.nombre, self.estado, self.direccion, self.telefono, self.credito)
    
    def getProveedor(self):
        return [str(self.codigo), self.nombre, str(self.estado), self.direccion, self.telefono, str(self.credito)]
    
    @staticmethod
    def getCredito():
        return True
    
if __name__  == '__main__':
    proveedor = Proveedor('Karen Marin', True, 'Milagro', '0934837438', True)
    print(proveedor.mostarDatos())
    print(Proveedor.getCredito())
    