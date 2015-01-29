'''
Created on 29/1/2015

@author: Tony
'''

import unittest
from taller.estacionamiento import Estacionamiento

class Test(unittest.TestCase):

    def testConstructor(self):
        empresa = Estacionamiento(3)
        self.assertEqual(empresa.capacidad, 3)
        self.assertEqual(empresa.tabla,[])
        
    def testAgregarIntervalo(self):
        empresa = Estacionamiento(3)
        empresa.agregarIntervalo(8, 13)
        self.assertEqual(empresa.tabla,[(8,-1),(13,1)])
        
    def testOrdenamientoVacio(self):
        empresa = Estacionamiento(3)
        empresa.ordenar()
        self.assertEqual(empresa.tabla,[])
        
    def testOrdenamiento(self):
        empresa = Estacionamiento(3)
        empresa.agregarIntervalo(8, 13)
        empresa.agregarIntervalo(10, 12)
        empresa.ordenar()
        self.assertEqual(empresa.tabla,[(8,-1),(10,-1),(12,1),(13,1)])
    
    def testOrdenamientoTiposIgualesOffSetsDistintos(self): 
        empresa = Estacionamiento(3)
        empresa.agregarIntervalo(8, 10)
        empresa.agregarIntervalo(6, 10)
        empresa.agregarIntervalo(10, 12)
        empresa.agregarIntervalo(10, 15)
        empresa.ordenar()
        self.assertEqual(empresa.tabla,[(6,-1),(8,-1),(10,-1),(10,-1),(10,1),(10,1),(12,1),(15,1)])
        
    def testViabilidadReservacion(self):
        empresa = Estacionamiento(10)
        empresa.agregarIntervalo(8, 11)
        empresa.agregarIntervalo(6, 10)
        empresa.ordenar()
        best,beststart,bestend = empresa.ViabilidadReservacion(15,16)
        self.assertEqual(best, 2, "Fallo en la variable best")
        self.assertEqual(beststart, 8, "Fallo en la variable beststart")
        self.assertEqual(bestend, 10, "Fallo en la variable bestend")
        
    def testAceptarReservacion(self):
        empresa = Estacionamiento(10)
        empresa.agregarIntervalo(8, 11)
        empresa.agregarIntervalo(6, 10)
        result = empresa.AceptarReservacion(9, 10)
        self.assertTrue(result)
        
    def testRechazarReservacion(self):
        empresa = Estacionamiento(2)
        empresa.AceptarReservacion(8, 11)
        empresa.AceptarReservacion(6, 10)
        result = empresa.AceptarReservacion(9, 10)
        self.assertFalse(result)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()