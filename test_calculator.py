# https://github.com/AadeshT/lab11-AT-ZZ.git
# Partner 1: Aadesh
# Partner 2: Zelun

import unittest
import calculator


class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(0, 0), 0)
        self.assertEqual(calculator.add(-5, 3), -2)

    def test_subtract(self):
        self.assertEqual(calculator.sub(5, 3), 2)
        self.assertEqual(calculator.sub(3, 5), -2)
        self.assertEqual(calculator.sub(0, 0), 0)

    ######### Partner 1
    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-3, 4), -12)
        self.assertEqual(calculator.mul(0, 5), 0)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5)
        self.assertEqual(calculator.div(-2, 10), -5)
        self.assertRaises(ZeroDivisionError, calculator.div, 0, 5)

    ######### Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.log(2, 8), 3)
        self.assertAlmostEqual(calculator.log(10, 100), 2)
        self.assertAlmostEqual(calculator.log(3, 27), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.log(1, 10)

    ######### Partner 1
    def test_log_invalid_argument(self):
        self.assertRaises(ValueError, calculator.log, 0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(-3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(0, 5), 5)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(9), 3)
        self.assertAlmostEqual(calculator.square_root(0), 0)
        self.assertRaises(ValueError, calculator.square_root, -9)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
