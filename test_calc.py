import unittest
from modules.calc import Calculator

class CalculatorTest(unittest.TestCase):
	
	def setUp(self):
		pass
		
	def test_number_3_4(self):
		calculator = Calculator()
		self.assertEqual( calculator.multiply(3,4), 12)
		
	def test_additional_3_4(self):
		calculator = Calculator()
		self.assertEquals( calculator.addition(3,4), 7)
		
if __name__ == '__main__':
	unittest.main()
