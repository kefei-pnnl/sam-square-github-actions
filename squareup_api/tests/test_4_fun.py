import unittest

class Test4Fun(unittest.TestCase):
    
    def test_4_fun(self):
        self.assertEqual(1+1,2)
        
    def test_4_fun_2(self): # fail on purpose
        self.assertEqual(1+1,4)
        
    