from datetime import date, datetime
from utileria.helpers import borrarPantalla, gotoxy, mensaje
import time

class Menu:
    def __init__(self,titulo="",opciones=[],col=6,fil=1):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
        
    def menu(self):
        gotoxy(self.col,self.fil);print(self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil +=1
            gotoxy(self.col,self.fil);print(opcion)
        gotoxy(self.col+5,self.fil+2)
        opc = input("Elija opcion[1...{}]:".format(len(self.opciones))) 
        return opc
    
class Valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*20)
        return valor

    def solo_letras(self,mensaje,mensajeError): 
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            if valor.isalpha():
                break
            else:
                print("          ------><  | {} ".format(mensajeError))
        return valor

    def solo_decimales(self,mensaje,mensajeError):
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                print("          ------><  | {} ".format(mensajeError))
        return valor
    
    def es_vacio(self,campo,col,fil, max_col_mesaje=17):
        mensaje = ' '
        while True:
            gotoxy(col,fil);valor=input()
            gotoxy(col+ max_col_mesaje,fil);print(' '*len(mensaje))
            if valor:
                break
            else:
                mensaje = f'Campo {campo} no puede Estar Vacio' 
                gotoxy(col+  max_col_mesaje,fil);print(mensaje)
            gotoxy(col,fil);print(' '*len(valor))
        return valor
    
    def es_booleano(self,campo,col,fil):
        mensaje = ' '
        while True:
            gotoxy(col,fil);valor=input()
            gotoxy(col+17,fil);print(' '*len(mensaje))
            if valor.lower() in ['v', 'f']:
                break
            else:
                mensaje = f'Campo {campo} debe elegir ["v", "V"] -> "Verdadero" ["f", "F"] -> "Falso"' 
                gotoxy(col+17,fil);print(mensaje)
            gotoxy(col,fil);print(' '*len(valor))
        return valor

    def solo_numeros_enteros(self,campo, col, fil, max_col_mesaje=17):
        mensaje = ' '
        while True: 
            gotoxy(col,fil);valor =self.es_vacio(campo,col,fil)
            gotoxy(col+max_col_mesaje,fil);print(' '*len(mensaje))
            try:
                valor = int(valor)
                if valor > 0:
                    break
            except:
                mensaje = f'Campo {campo} No es Un Numero Entero'
                gotoxy(col+max_col_mesaje,fil);print(mensaje)
                time.sleep(1)
            gotoxy(col,fil);print(' '*len(str(valor)))
        return valor

    def solo_numeros_mayores_con_0(self,campo,col,fil):
        mensaje = ' '
        while True: 
            gotoxy(col,fil);valor =self.es_vacio(campo,col,fil)
            gotoxy(col+17,fil);print(' '*len(mensaje))
            try:
                valor = int(valor)
                if valor >= 0:
                    break
            except:
                mensaje = f'Campo {campo} No es Un Numero Entero'
                gotoxy(col+17,fil);print(mensaje)
                time.sleep(1)
            gotoxy(col,fil);print(' '*len(str(valor)))
        return valor

    def solo_decimales_1(self, campo, col, fil, max_col_mesaje=17):
        mensaje = ' '
        while True: 
            gotoxy(col,fil); valor =self.es_vacio(campo,col,fil)
            gotoxy(col+max_col_mesaje,fil);print(' '*len(mensaje))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                mensaje = f'Campo {campo} No es Un Decimal'
                gotoxy(col+max_col_mesaje,fil);print(mensaje)
                time.sleep(1)
            gotoxy(col,fil);print(' '*len(str(valor)))
        return valor

    def valido_cadena(self,campo,col,fil):
        mensaje = ''
        while True: 
            gotoxy(col,fil);valor =self.es_vacio(campo,col,fil)
            gotoxy(col+17,fil);print(' '*len(mensaje))
            try:
                valor_entero = int(valor.replace('0','') if valor.find('0') else valor)
                if valor_entero >= 0:
                    break
            except:
                mensaje = f'Campo {campo} No es Un Numero Entero'
                gotoxy(col+17,fil);print(mensaje)
                time.sleep(1)
            gotoxy(col,fil);print(' '*len(str(valor)))
        return valor

    def cedula(self,campo,col,fil,listado_archivo):
        mensaje = ' '
        while True:
            valor = self.valido_cadena(campo,col,fil)
            gotoxy(col+17,fil);print(' '*len(mensaje))
            if len(valor) == 10:
                listado =listado_archivo.buscar(valor,5)
                if listado :
                    mensaje = f'{campo} ya se encuentra registrado'
                    gotoxy(col+17,fil);print(mensaje)
                else:
                    break
            else:
                mensaje = f'{campo} Invalida, el debe contener 10 caracteres no {len(valor)}'
                gotoxy(col+17,fil);print(mensaje)
                
            gotoxy(col,fil);print(' '*len(valor))
        return valor

    def ruc(self,campo,col,fil,listado_archivo):
        mensaje = ' '
        while True:
            valor = self.valido_cadena(campo,col,fil)
            gotoxy(col+17,fil);print(' '*len(mensaje))
            if len(valor) == 13:
                listado =listado_archivo.buscar(valor)
                if listado :
                    mensaje = f'{campo} ya se encuentra registrado'
                    gotoxy(col+17,fil);print(mensaje)
                else:
                    break
            else:
                mensaje = f'{campo} Invalida, el debe contener 13 caracteres no {len(valor)}'
                gotoxy(col+17,fil);print(mensaje)
                
            gotoxy(col,fil);print(' '*len(valor))
        return valor

    def telefono(self,campo,col,fil):
        mensaje = ' '
        while True:
            valor = self.valido_cadena(campo,col,fil)
            gotoxy(col+17,fil);print(' '*len(mensaje))
            if len(valor) == 10:
                break
            else:
                mensaje = f'{campo} Invalida, el debe contener 10 caracteres no {len(valor)}'
                gotoxy(col+17,fil);print(mensaje)
                
            gotoxy(col,fil);print(' '*len(valor))
        return valor
    def id(self,campo,col,fil,listado_archivo,posicion =0):
        mensaje = ' '
        while True:
            gotoxy(col,fil);valor = self.solo_numeros_mayores_con_0(campo,col,fil)
            listado = listado_archivo.buscar(str(valor),posicion)
            gotoxy(col+17,fil);print(' '*len(mensaje))
            if valor == 0:
                gotoxy(col,fil);print(f'Sin {campo}')
                valor = [valor,f'Sin {campo}']
                break
            elif valor and listado:
                gotoxy(col,fil);print(listado[1])
                valor = listado
                break
            elif not (listado) :
                mensaje = f'{campo} no existe'
                gotoxy(col+17,fil);print(mensaje)
            gotoxy(col,fil);print(' '*len(str(valor)))
        return valor

    def opcion(self,campo,col,fil):
        mensaje = ' '
        while True:
            gotoxy(col,fil);valor =input()
            gotoxy(col+17,fil);print(' '*len(mensaje))
            valor = valor.lower()
            if valor == 's' or valor == 'n' :
                break
            else:
                mensaje = f'EL Campo {campo} solo admite 1 caracter ("s","n") o ("S","N") ' 
                gotoxy(col+17,fil);print(mensaje)
            gotoxy(col,fil);print(' '*len(valor))
        return valor

    def opcion_obr_admin(self,col,fil, max_col_mesaje=17):
        mensaje = ' '
        while True:
            gotoxy(col,fil);valor =input()
            gotoxy(col+17,fil);print(' '*len(mensaje))
            valor = valor.lower()
            if valor == 'o' or valor == 'a' :
                break
            else:
                mensaje = f'solo admite 1 caracter ("O","A") o ("o","a") ' 
                gotoxy(col+27,fil);print(mensaje)
            gotoxy(col,fil);print(' '*len(valor))
        return valor

    def fecha(self, campo, col, fil,  max_col_mensaje=17):
        mensaje = ' '
        while True: 
            gotoxy(col,fil); valor =self.es_vacio(campo,col,fil, max_col_mensaje)
            gotoxy(col+max_col_mensaje,fil);print(' '*len(mensaje))
            try:
                valor = datetime.strptime(valor, '%Y-%m-%d').date()
                break
            except:
                mensaje = f'Campo {campo} Invalido,El formato que el acepta es aaaa-mm-dd'
                gotoxy(col+max_col_mensaje,fil);print(mensaje)
                time.sleep(1)
            gotoxy(col,fil);print(' '*len(str(valor)))
        return valor
    
    def fecha_anio_mes(self, campo, col, fil,  max_col_mensaje=17):
        mensaje = ' '
        while True: 
            gotoxy(col,fil); valor = input()
            gotoxy(col+max_col_mensaje,fil);print(' '*len(mensaje))
            if valor  in ['t', 'T']:
                return valor
            try:
                valor = datetime.strptime(valor, '%Y-%m').date()
                break
            except:
                mensaje = f'Campo {campo} Invalido,El formato que el acepta es aaaa-mm o digite ["t", "T"] para consultar todas las fechas'
                gotoxy(col+max_col_mensaje,fil);print(mensaje)
                time.sleep(1)
            gotoxy(col,fil);print(' '*len(str(valor)))
        return valor