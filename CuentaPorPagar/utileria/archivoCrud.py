import os
sys_ar = os.path

class Archivo:
    def __init__(self,nombreArchivo,separador=';'):
        self.__archivo = nombreArchivo
        self.__separador = separador
        os.makedirs("./datos", exist_ok=True)
        if not (sys_ar.isfile(nombreArchivo)):
            open(nombreArchivo,'w+')
            
    @property    
    def separador(self):
      return self.__separador
    
    @property    
    def archivo(self):
      return self.__archivo
    
    def leer(self):
        try:
          with open(self.__archivo, 'r', encoding="UTF-8") as file:
            lista=[] 
            for linea in file:
              line = linea[:-1].split(self.__separador)
              lista.append(line)
        except IOError:
           lista=[]    
        return lista       
    
    def buscar(self,buscado,posicion = 0): 
        resultado = [] 
                      
        with open(self.archivo, mode='r', encoding='utf-8') as file:
            for linea in file:
               if linea[:-1].split(self.separador)[posicion].find(buscado) is not -1 :
                    resultado = linea[:-1].split(self.separador)
        return resultado
   
    def buscarLista(self,buscado,posicion=0, busqueda_exacta=True):
        resultado = []
        with open(self.__archivo, mode='r', encoding='utf-8') as file:
            for linea in file:
                registro = linea[:-1].split(self.__separador) 
                if registro[posicion] == buscado and busqueda_exacta:
                  resultado.append(registro)
                if registro[posicion].find(buscado) is not -1 and not busqueda_exacta:
                  resultado.append(registro)
        return resultado
     
    def buscar2(self,buscado1,buscado2):
        resultado = []
        with open(self.__archivo, mode='r', encoding='utf-8') as file:
            for linea in file:
                registro = linea[:-1].split(self.__separador) 
                if registro[1] == buscado1 and registro[2] == buscado2:
                    resultado = registro
        return resultado

    def escribir(self,datos,modo):
         with open(self.__archivo, modo, encoding="UTF-8") as file:
           for dato in datos:
             file.write(dato+'\n')
             
    def escribirM(self,datos,modo):
      with open(self.__archivo, modo, encoding="UTF-8") as file:
        for dato in datos:
          linea=''
          for valor in dato:
            if type(valor) == int or float: linea +=str(valor)+self.__separador
            else: linea += valor + self.__separador     
          file.write(linea[:-1]+"\n")            
