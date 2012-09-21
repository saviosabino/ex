import unittest
import calc

class TestCalc(unittest.TestCase):
  def testMult(self):
    self.assertEqual(calc.multi([2,3,4]),24)

def run():
    unittest.main()

if __name__ == '__main__':
    unittest.main()

