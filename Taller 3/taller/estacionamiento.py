'''
Created on 29/1/2015

@author: Tony
'''
class FueraDeHorario(Exception):
    
    def __init__(self):
        self.msg = "Los intervalos ingresados no se encuentran dentro del horario de trabajo"


class Estacionamiento:
    
    def __init__(self,capacidad):
        self.capacidad = capacidad
        self.tabla = []
    
    def validarEnteros(self,x,y):
        if (isinstance(x, int) != False) or ( isinstance(y, int) != False) :  
            try:
                print("Intervalos deben ser de tipo entero")
                raise TypeError()
            except TypeError:
                raise
        
    def agregarIntervalo(self,x,y):
        if (x>=6) and (y<=18) :
            self.tabla.append((x,-1))
            self.tabla.append((y,1))
        else :
            try:
                print("Reserva fuera del horario de trabajo")
                raise FueraDeHorario()
            except FueraDeHorario:
                raise
            
    def ordenar(self):
        
        def obtenerClave(item):
            return item[0],item[1]
        
        self.tabla = sorted(self.tabla, key = obtenerClave)
        
        
    def ViabilidadReservacion(self,x,y):
        
        # Devuelve True si un solapamiento se encuentra dentro del rango de una reservacion
        # False en caso contrario
        def SolapamientoEnRangoReserva(x,y,inicio,fin):
            if ((x in range(inicio,fin+1)) or (y in range(inicio,fin+1))):
                return True
            return False
        
        tipo = 0
        offset = 1
        best = 0
        cnt = 0
        beststart = 0
        bestend = 0
        for i in range(0,len(self.tabla)):
            cnt = cnt - self.tabla[i][offset]
            if (cnt > best) and (self.tabla[i][tipo] != self.tabla[i+1][tipo]) :
                best = cnt
                beststart = self.tabla[i][tipo]
                bestend = self.tabla[i+1][tipo]
            elif (cnt == best) and SolapamientoEnRangoReserva(x, y,self.tabla[i][tipo],self.tabla[i+1][tipo]) :
                best = cnt
                beststart = self.tabla[i][tipo]
                bestend = self.tabla[i+1][tipo]
        return best,beststart,bestend
    
    def AceptarReservacion(self,x,y):
        self.ordenar()
        best,beststart,bestend = self.ViabilidadReservacion(x, y)
        if best < self.capacidad : 
            self.agregarIntervalo(x, y)
            return True
        elif best == self.capacidad :
            # Si el rango del solapamiento intersecta el de la reservacion, no se acepta esta ultima
            if ((x in range(beststart,bestend) or (y in range(beststart,bestend+1)))) :
                return False
            else :
                self.agregarIntervalo(x, y)
                return True
        return False