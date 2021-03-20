import unittest
from src import calc


class TestCalc(unittest.TestCase):
    """"""

    @classmethod
    def setUpClass(cls):
        """"""
        cls.PASS = '\x1b[6;30;42m'
        cls.INFO = '\x1b[6;30;43m'
        cls.STOP = '\x1b[0m'

        print(cls.INFO + "Initializing variables." + cls.STOP)
    
    @classmethod
    def setUpClass(cls):
        """"""
        print(cls.INFO + "Cleaning up" + cls.STOP)

    def test_add(self):
        """Test the add function.."""
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-14, 5), -9)
        self.assertEqual(calc.add(-2, -3), -5)
        print(
            self.PASS + "Add function tested successfully."
            + self.STOP
        )

    def test_subtract(self):
        """Test the subtract function.."""
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-14, 5), -19)
        self.assertEqual(calc.subtract(-2, -3), 1)
        print(
            self.PASS + "Subtract function tested successfully."
            + self.STOP
        )

    def test_multiply(self):
        """Test the multiply function.."""
        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(-5, 9), -45)
        self.assertEqual(calc.multiply(-2, -3), 6)
        print(
            self.PASS + "Multpily function tested successfully."\
                + self.STOP
        )

    def test_divide(self):
        """Test the divide function.."""
        self.assertEqual(calc.divide(12, 4), 3.0)
        self.assertEqual(calc.divide(-21, 7), -3)
        self.assertEqual(calc.divide(-15, -3), 5)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)
        
        print(
            self.PASS + "Divide function tested successfully." \
                + self.STOP
        )

if __name__ == '__main__':
    unittest.main()
