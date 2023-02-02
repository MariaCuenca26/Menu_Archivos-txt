from utileria.archivoCrud import Archivo
from utileria.componente import Menu, Valida
from utileria.helpers import borrarPantalla, gotoxy
from utileria.tableUi import printTable


def consultas():
    borrarPantalla()
    opc = ''
    validar = Valida()
    while opc != '4':
        borrarPantalla()
        menu  = Menu("Menú Consultas", ["1) Búsqueda por proveedores o fecha compra.", "2) Búsqueda de deudas por fecha crédito",  "3) Búsqueda de deuda por código",  "4) Salir"])
        opc = menu.menu()
        borrarPantalla()
        if opc == '1':
            gotoxy(1,1);print('***************** BUSCAR COMPRAS *****************')
            gotoxy(1,3);print('Proveedor..:')
            gotoxy(1,4);print('Fecha......:')
            archiProveedor = Archivo("./datos/proveedor.txt","|")
            archiCompra = Archivo("./datos/compra.txt","|")
            gotoxy(13,3);proveedor = input()
            gotoxy(13,4);fecha = input()
            compras = archiCompra.leer()
            registro_proveedor = archiProveedor.buscar(proveedor)
            if len(registro_proveedor) > 0 and  fecha:
                compras_fecha  = archiCompra.buscarLista(fecha, 2, busqueda_exacta=False)
                compras = [compra for compra  in compras_fecha if compra[1] == proveedor]
            elif proveedor:
                compras  = archiCompra.buscarLista(proveedor, 1)
            elif fecha:
                compras  = archiCompra.buscarLista(proveedor, 2)
            tabla = []
            tabla.append(['Código', 'Proveedor', 'Fecha Compra', 'Total', 'Estado'])
            for compra  in compras:
                proveedor = archiProveedor.buscar(compra[1])
                tabla.append([compra[0], proveedor[1], compra[2], compra[3], compra[4]])
                
            printTable(tabla, useFieldNames=True,color=(26, 156, 171))
            gotoxy(1,len(compras)+10);print("Presiona cualquier tecla para regresar al ménu....")
            gotoxy(55,len(compras)+10);input()   
        
        if opc == '2':
            gotoxy(1,1);print('***************** BUSCAR DEUDAS*****************')
            gotoxy(1,3);print('Fecha Credito......:')
            fecha = validar.fecha_anio_mes('Fecha Credito', 21, 3)
            archiDeuda = Archivo("./datos/deuda.txt","|")
            archiCompra = Archivo("./datos/compra.txt","|")
            archiProveedor = Archivo("./datos/proveedor.txt","|")
            deudas  = archiDeuda.leer()
            mensaje = """                                 LISTADO TODAS LAS DEUDAS          """
            if not fecha in ['t', 'T']:
                fechatemp = fecha.strftime('%Y-%m')
                deudas = archiDeuda.buscarLista(fechatemp, 2, busqueda_exacta=False)
                MESES = ['ENERO', 'FEBRERO',
                      'MARZO', 'ABRIL', 
                      'MAYO', 'JUNIO', 
                      'JULIO', 'AGOSTO', 
                      'SEPTIMBRE', 'OCTUBRE', 
                      'NOVIEMBRE', 'DICIEMBRE', 
                      ]
                mensaje = f"""                 LISTADO DE TODAS LAS DEUDAS  DEL AÑO {fecha.year} DEL MES DE {MESES[fecha.month-1]}       """
                
            print(mensaje)
            tabla = []
            tabla.append(['Código', 'Proveedor', '#Compra', 'F.Compra', 'F.Credito', 'Valor Credito', '#Cuotas', 'Valor Cuota', 'F. Inicio Pago', 'Pagado'])
            for deuda  in deudas:
                compra = archiCompra.buscar(deuda[1])
                proveedor = archiProveedor.buscar(compra[1])
                tabla.append([deuda[0], proveedor[1], deuda[1], compra[2], deuda[2], deuda[3], deuda[4], deuda[5], deuda[6], 'Si' if deuda[7] == 'True' else 'No'])
            printTable(tabla, useFieldNames=True,color=(26, 156, 171))
            gotoxy(1,len(deudas)+12);print("Presiona cualquier tecla para regresar al ménu....")
            gotoxy(55,len(deudas)+12);input()   
            
        if opc == '3':
            gotoxy(1,1);print('***************** BUSCAR DEUDA POR CÓDIGO*****************')
            gotoxy(1,3);print('Código......:')
            deuda_id = validar.solo_numeros_enteros('Código', 21, 3)
            archiDeuda = Archivo("./datos/deuda.txt","|")
            archiCompra = Archivo("./datos/compra.txt","|")
            archiProveedor = Archivo("./datos/proveedor.txt","|")
            archiDetalleDeuda = Archivo("./datos/detalle_deuda.txt","|")
            registro = archiDeuda.buscar(str(deuda_id))
            if len(registro) > 0:
                compra = archiCompra.buscar(registro[1])
                proveedor = archiProveedor.buscar(compra[1])
                gotoxy(1,6);print('***************** CREAR DEUDA *****************')
                
                gotoxy(1,7);print(f'Deuda#.....: {registro[0]}')
                gotoxy(1,8);print(f'Compra.....: {registro[1]}')
                gotoxy(1,9);print(f'F.Credito..: {registro[2]}')
                
                gotoxy(27,7);print(f'F.Compra......: {compra[2]}')
                gotoxy(27,8);print(f'ValorCredito..: {registro[3]}')
                gotoxy(27,9);print(f'NoCuotas......: {registro[4]}')
                
                gotoxy(54,7);print(f'ValorCuota....: {registro[5]}')
                gotoxy(54,8);print(f'F.PagoIni.....: {registro[6]}')
                gotoxy(54,9);print(f'Proveedor.....: {proveedor[1]}')
                
                detalles = archiDetalleDeuda.buscarLista(registro[0])
                tabla = []
                tabla.append(['Código' ,'Cuota', 'Fecha', 'Pagado'])
                for detList  in detalles:
                    detList[-1] = 'Si' if detList[-1] ==  'True' else 'No' 
                    tabla.append(detList)
                
                printTable(tabla, useFieldNames=True,color=(26, 156, 171))   
                medida = len(detalles)+12
                gotoxy(1,medida);print("Presiona cualquier tecla para regresar al ménu....")
                gotoxy(55,medida);input()
            else:
                gotoxy(1,7);print(f'No existen deuda con código {deuda_id}') 
                gotoxy(1,9);print("Presiona cualquier tecla para regresar al ménu....")
                gotoxy(55,9);input()