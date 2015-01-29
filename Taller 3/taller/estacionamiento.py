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