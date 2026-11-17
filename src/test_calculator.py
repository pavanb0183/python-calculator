import unittest

from calculator import calculator


class TestCalculator(unittest.TestCase):
	def test_addition(self):
		self.assertEqual(calculator("add", 2, 3), 5)

	def test_subtraction(self):
		self.assertEqual(calculator("subtract", 5, 2), 3)

	def test_multiplication(self):
		self.assertEqual(calculator("multiply", 2, 3), 6)

	def test_division(self):
		self.assertEqual(calculator("divide", 6, 2), 3)

	def test_division_by_zero(self):
		with self.assertRaises(ValueError):
			calculator("divide", 6, 0)

	def test_invalid_operation(self):
		with self.assertRaises(ValueError):
			calculator("modulo", 2, 3)


if __name__ == "__main__":
	unittest.main()
