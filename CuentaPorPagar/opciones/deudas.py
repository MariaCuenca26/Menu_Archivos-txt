from datetime import timedelta, datetime
from dateutil.relativedelta import  relativedelta
from clases.compra import Compra
from clases.deuda import Deuda
from utileria.tableUi import printTable
from utileria.archivoCrud import Archivo
from clases.proveedor import Proveedor
from utileria.componente import Menu, Valida
from utileria.helpers import borrarPantalla, gotoxy

def deudas():
    borrarPantalla()
    opc = ''
    validar = Valida()
    while opc != '3':
        borrarPantalla()
        menu  = Menu("Menú Deuda", ["1) Ingreso", "2) Listado",  "3) Salir"])
        opc = menu.menu()
        borrarPantalla()
        if opc == '1':
            gotoxy(1,1);print('***************** CREAR DEUDA *****************')
            gotoxy(1,3);print('Deuda#.....:')
            gotoxy(1,4);print('Compra.....:')
            gotoxy(1,5);print('F.Credito..:')
            

            gotoxy(27,3);print('F.Compra......:')
            gotoxy(27,4);print('ValorCredito..:')
            gotoxy(27,5);print('NoCuotas......:')
            
            gotoxy(54,3);print('ValorCuota....:')
            gotoxy(54,4);print('F.PagoIni.....:')
            gotoxy(54,5);print('Proveedor.....:')
            
            archiDeuda = Archivo("./datos/deuda.txt","|")
            archiCompra = Archivo("./datos/compra.txt","|")
            archiProveedor = Archivo("./datos/proveedor.txt","|")
            deudas = archiDeuda.leer()
            if deudas : idSig = int(deudas[-1][0])+1
            else: idSig=1
            gotoxy(14,3);print(idSig)
            registro = []
            fecha_compra = ''
            valorCredito = 0.0
            while registro == []:
                gotoxy(14,4);deuda = input()
                registro = archiCompra.buscar(deuda)
                if registro:
                    if len(deuda) > len(registro[1]):
                        l =len(deuda) - len(registro[1])
                        gotoxy(43+len(registro[2]),3);print(' '*l)
                        gotoxy(43+len(registro[3]),4);print(' '*l)
                    fecha_compra = registro[2]
                    gotoxy(43,3);print(fecha_compra)
                    valorCredito = float(registro[3])
                    gotoxy(43,4);print(valorCredito)
                else: 
                    gotoxy(14,4);print(' '*len(deuda))
            registro_proveedor = archiProveedor.buscar(registro[1])
            gotoxy(71,5);print(registro_proveedor[1])
            fecha_credito = validar.fecha('F.Credito', 14, 5, 75)
            num_cuotas = validar.solo_numeros_enteros('NoCuotas', 43, 5, 30)   
            valorCuota =  round(valorCredito/ num_cuotas, 2)
            gotoxy(71,3);print(valorCuota)
            fecha_pago = validar.fecha('F.PagoIni', 71, 4, 30)
            proveedor = Proveedor(registro_proveedor[1], 
                                  registro_proveedor[2], 
                                  registro_proveedor[3], 
                                  registro_proveedor[4], 
                                  registro_proveedor[5], 
                                  int(registro_proveedor[0]))
            deuda = Compra(proveedor, registro[2], registro[3], registro[4], int(registro[0]))
            deuda = Deuda(deuda, str(fecha_credito), valorCredito, num_cuotas, valorCuota, str(fecha_pago), id=idSig)
            tabla = []
            tabla.append(['Código' ,'Cuota', 'Fecha', 'Pagado'])
            archiDetalleDeuda = Archivo("./datos/detalle_deuda.txt","|")
            detalleDeudas = archiDetalleDeuda.leer()
            if detalleDeudas : idSig = int(detalleDeudas[-1][0])+1
            else: idSig=1
            fecha_pago_detalle = datetime.strptime(str(fecha_pago), '%Y-%m-%d')
            for cuota  in range(1, num_cuotas + 1):
                deuda.agregarDetalleDeuda(str(fecha_pago_detalle.date()), valorCuota, id=deuda.codigo)
                idSig += 1 
                fecha_pago_detalle = fecha_pago_detalle + relativedelta(months=1)
            
            for detalle  in deuda.detDeuda:
                detList = detalle.getDetalleDeuda()
                detList[-1] = 'Si' if detList[-1] ==  'True' else 'No' 
                tabla.append(detList)
                
            printTable(tabla, useFieldNames=True,color=(26, 156, 171))       
            medida = len(deuda.detDeuda)+10
            gotoxy(0, medida);print("Esta seguro de Grabar El registro(s/n):")
            gotoxy(41, medida);grabar = input().lower()
            if grabar == "s":
                datos = deuda.getDeuda()
                datos = '|'.join(datos)
                archiDeuda.escribir([datos],"a")
                for detalle in deuda.detDeuda:
                    datos = detalle.getDetalleDeuda()
                    datos = '|'.join(datos)
                    archiDetalleDeuda.escribir([datos],"a")
                gotoxy(15,medida+1);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
            else:
                gotoxy(27, medida+1);input("Registro No fue Grabado\n presione una tecla para continuar...")
            
            
        if opc == '2':
            archiDeuda = Archivo("./datos/deuda.txt","|")
            archiCompra = Archivo("./datos/compra.txt","|")
            archiProveedor = Archivo("./datos/proveedor.txt","|")
            deudas = archiDeuda.leer()
            print("""                                 LISTADO DEUDAS          """)
            tabla = []
            tabla.append(['Código', 'Proveedor', '#Compra', 'F.Compra', 'F.Credito', 'Valor Credito', '#Cuotas', 'Valor Cuota', 'F. Inicio Pago', 'Pagado'])
            for deuda  in deudas:
                compra = archiCompra.buscar(deuda[1])
                proveedor = archiProveedor.buscar(compra[1])
                tabla.append([deuda[0], proveedor[1], deuda[1], compra[2], deuda[2], deuda[3], deuda[4], deuda[5], deuda[6], 'Si' if deuda[7] == 'True' else 'No'])
                
            printTable(tabla, useFieldNames=True,color=(26, 156, 171))
            gotoxy(1,len(deudas)+10);print("Presiona cualquier tecla para regresar al ménu....")
            gotoxy(55,len(deudas)+10);input()