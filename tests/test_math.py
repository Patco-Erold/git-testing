import unittest
from src import calc


class TestCalc(unittest.TestCase):
    """"""

    def test_add(self):
        """Test the add function.."""
        self.assertEquals(calc.add(10, 5), 15)
        self.assertEquals(calc.add(-14, 5), -9)
        self.assertEquals(calc.add(-2, -3), -5)

    def test_subtract(self):
        """Test the subtract function.."""
        self.assertEquals(calc.subtract(10, 5), 5)
        self.assertEquals(calc.subtract(-14, 5), -19)
        self.assertEquals(calc.subtract(-2, -3), 1)

    def test_multiply(self):
        """Test the multiply function.."""
        self.assertEquals(calc.multiply(2, 3), 6)
        self.assertEquals(calc.multiply(-5, 9), -45)
        self.assertEquals(calc.multiply(-2, -3), 6)

    def test_divide(self):
        """Test the divide function.."""
        self.assertEquals(calc.divide(12, 4), 3.0)
        self.assertEquals(calc.divide(-21, 7), -3)
        self.assertEquals(calc.divide(-15, -3), 5)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)
