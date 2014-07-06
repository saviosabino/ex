import unittest
import celsiusFahren

class TestCF(unittest.TestCase):
  def setUp(self):
    self.cf = celsiusFahren.CF()

  def testCtoF(self):
    self.assertEqual(86,self.cf.cf(30))

  def testFtoC(self):
    self.assertEqual(65,self.cf.fc(149))    

if __name__ == '__main__':
  unittest.main()
