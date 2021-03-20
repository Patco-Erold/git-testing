import unittest
from src import calc


class TestCalc(unittest.TestCase):
    """"""

    def test_add(self):
        """Test the add function.."""
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-14, 5), -9)
        self.assertEqual(calc.add(-2, -3), -5)

    def test_subtract(self):
        """Test the subtract function.."""
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-14, 5), -19)
        self.assertEqual(calc.subtract(-2, -3), 1)

    def test_multiply(self):
        """Test the multiply function.."""
        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(-5, 9), -45)
        self.assertEqual(calc.multiply(-2, -3), 6)

    def test_divide(self):
        """Test the divide function.."""
        self.assertEqual(calc.divide(12, 4), 3.0)
        self.assertEqual(calc.divide(-21, 7), -3)
        self.assertEqual(calc.divide(-15, -3), 5)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()