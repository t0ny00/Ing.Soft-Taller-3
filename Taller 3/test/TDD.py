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
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()