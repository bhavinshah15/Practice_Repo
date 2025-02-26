from Package1 import my_math
import unittest

class TestMyMath(unittest.TestCase):
    def setup(self):
        print("Inside TestMyMath : setup()")
        self.a=10
        self.b=5

    def tearDown(self):
        print("Inside TestMyMath : tearDown()")
        self.a=None
        self.b=None

    def test_add_positive():
        print("Inside TestMyMath : test_add_positive()")
        self.assertEqual(my_add(self.a,self.b), 15)
