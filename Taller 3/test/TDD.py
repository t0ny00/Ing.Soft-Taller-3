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
        
    
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()