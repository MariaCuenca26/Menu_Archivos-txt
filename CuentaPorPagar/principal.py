from utileria.componente import Menu
from utileria.helpers import borrarPantalla
from opciones.compras import compras
from opciones.consultas import consultas
from opciones.deudas import deudas
from opciones.proveedores import proveedores



opc = ''
while opc != '5':
    borrarPantalla()
    menu  = Menu("Menú Principal", ["1) Proveedor", "2) Compra", "3) Debt cuotas", "4) Consulta generales", "5) Salir"])
    opc = menu.menu()
    if opc == "1": proveedores()        
    elif opc == "2":compras()
    elif opc == "3":deudas()
    elif opc == "4":consultas()
    elif opc == "5":
        borrarPantalla()
        print("Gracias por su visita....")
    else:
        print("Opcion no valida") 
        
        
        
        