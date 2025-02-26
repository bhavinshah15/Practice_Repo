from Package1 import my_math
import unittest

class TestMyMath(unittest.TestCase):
    def setUp(self):
        print("Inside TestMyMath : setup()")
        self.a=10
        self.b=5

    def tearDown(self):
        print("Inside TestMyMath : tearDown()")
        self.a=None
        self.b=None

    def test_add_positive(self):
        print("Inside TestMyMath : test_add_positive()")
        self.assertEqual(my_math.my_add(self.a,self.b), 15)

    def test_divide_by_zero(self):
        print("Inside TestMyMath : test_divide_by_zero()")
        with self.assertRaise(ValueError):
            my_math.my_divide(self.a,0)

if __name__=='__main__':
    unittest.main()

