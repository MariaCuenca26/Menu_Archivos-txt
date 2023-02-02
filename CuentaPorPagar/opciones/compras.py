from datetime import date
from utileria.archivoCrud import Archivo
from clases.proveedor import Proveedor
from utileria.componente import Menu, Valida
from utileria.helpers import borrarPantalla, gotoxy
from clases.compra import Compra
from utileria.tableUi import printTable


def compras():
    borrarPantalla()
    opc = ''
    validar = Valida()
    while opc != '3':
        borrarPantalla()
        menu  = Menu("Menú Compra", ["1) Ingreso", "2) Listado",  "3) Salir"])
        opc = menu.menu()
        borrarPantalla()
        if opc == '1':
            gotoxy(1,1);print('***************** Crear Compra *****************')
            gotoxy(1,2);print('Compra..:')
            gotoxy(1,3);print('Fecha..:')
            gotoxy(1,4);print('Proveedor..:')
            gotoxy(1,5);print('Total......:')
            archiCompra = Archivo("./datos/compra.txt","|")
            compras = archiCompra.leer()
            if compras : idSig = int(compras[-1][0])+1
            else: idSig=1
            gotoxy(13,2);print(idSig)
            fecha = validar.fecha('Fecha',13, 3)
            registro = []
            archiProveedor = Archivo("./datos/proveedor.txt","|")
            while registro == []:
                gotoxy(13,4);proveedor = input()
                registro = archiProveedor.buscar(proveedor)
                if registro:
                    if len(proveedor) > len(registro[1]):
                        l =len(proveedor) - len(registro[1])
                        gotoxy(13+len(registro[1]),4);print(' '*l)
                    gotoxy(13,4);print(registro[1])
                else: gotoxy(13,4);print(' '*len(proveedor))
            gotoxy(13,5);total = input()
            
            #['1', 'Maggi', 'True', 'Milagro', '0924390024', 'True']
            proveedor = Proveedor(registro[1], registro[2], registro[3], registro[4], registro[5], int(registro[0]))
            compra = Compra(proveedor, str(fecha), total,id=idSig)
            datos = compra.getCompra()
            datos = '|'.join(datos)
            gotoxy(27,7);print("Esta seguro de Grabar El registro(s/n):")
            gotoxy(67,7);grabar = input().lower()
            if grabar == "s":
                archiCompra.escribir([datos],"a")
                gotoxy(15,8);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
            else:
                gotoxy(27,8);input("Registro No fue Grabado\n presione una tecla para continuar...")
        if opc == '2':
            archiCompra = Archivo("./datos/compra.txt","|")
            archiProveedor = Archivo("./datos/proveedor.txt","|")
            compras = archiCompra.leer()
            print("""                                 LISTADO COMPRAS          """)
            tabla = []
            tabla.append(['Código', 'Proveedor', 'Fecha Compra', 'Total', 'Estado'])
            for compra  in compras:
                proveedor = archiProveedor.buscar(compra[1])
                tabla.append([compra[0], proveedor[1], compra[2], compra[3], compra[4]])
                
            printTable(tabla, useFieldNames=True,color=(26, 156, 171))
            gotoxy(1,len(compras)+7);print("Presiona cualquier tecla para regresar al ménu....")
            gotoxy(55,len(compras)+7);input()