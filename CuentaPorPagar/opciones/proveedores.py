from utileria.archivoCrud import Archivo
from  utileria.helpers import borrarPantalla, gotoxy
from utileria.tableUi import printTable
from utileria.componente import Menu, Valida
from clases.proveedor import Proveedor

def proveedores():
    borrarPantalla()
    opc = ''
    validar = Valida()
    while opc != '3':
        borrarPantalla()
        menu  = Menu("Menú Proveedor", ["1) Nuevo", "2) Listado",  "3) Salir"])
        opc = menu.menu()
        borrarPantalla()
        if opc == '1':
            gotoxy(10,2);print("***************** Crear Proveedor *****************")
            gotoxy(10,4);print("Código........:")
            gotoxy(10,5);print("Nombre........:")
            gotoxy(10,6);print("Dirección.....:")
            gotoxy(10,7);print("Teléfono......:")
            gotoxy(10,8);print("Crédito.......:")
            archiProveedor = Archivo("./datos/proveedor.txt","|")
            proveedores = archiProveedor.leer()
            if proveedores : idSig = int(proveedores[-1][0])+1
            else: idSig=1
            gotoxy(27,4);print(idSig)
            nombre = validar.es_vacio('Nombre', 27, 5)
            direccion = validar.es_vacio('Dirección', 27, 6)
            telefono = validar.es_vacio('Télefono', 27, 7)
            credito = validar.es_booleano('Crédito', 27, 8)
            credito = credito.lower() == 'v'
            proveedor = Proveedor(nombre, True, direccion, telefono, credito, id=idSig)
            datos = proveedor.getProveedor()
            datos = '|'.join(datos)
            gotoxy(27,10);print("Esta seguro de Grabar El registro(s/n):")
            gotoxy(67,10);grabar = input().lower()
            if grabar == "s":
                archiProveedor.escribir([datos],"a")
                gotoxy(27,12);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
            else:
                gotoxy(27,12);input("Registro No fue Grabado\n presione una tecla para continuar...") 

        elif opc == '2':
            archiProveedor = Archivo("./datos/proveedor.txt","|")
            proveedores = archiProveedor.leer()
            #print(proveedores)
            print("""                                 LISTADO PROVEEDORES          """)

            tabla = []
            tabla.append(['Código', 'Nombre', 'Estado', 'Dirección', 'Télefono', 'Crédito'])
            for dato in proveedores:
                #tabla.append(['\x1b[0;34m'+dato[0],'\x1b[0;34m'+dato[1],'\x1b[0;34m'+dato[2],'\x1b[0;34m'+dato[3],'\x1b[0;34m'+dato[4],'\x1b[0;34m'+dato[5]])
                tabla.append([dato[0],dato[1], dato[2], dato[3], dato[4], dato[5]])
            #tabla.append([proveedores])
            printTable(tabla, useFieldNames=True,color=(26, 156, 171))
            gotoxy(1,len(proveedores)+7);print("Presiona cualquier tecla para regresar al ménu....")
            gotoxy(55,len(proveedores)+7);input()