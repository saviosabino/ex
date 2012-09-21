import unittest
import logic

class TestLogic(unittest.TestCase):
   def testOutput(self):
        t9 = logic.T9('test.in')
        t9.writeN()
        expect = logic.CodeJam('expect.out')
        out = logic.CodeJam('test.out')
        self.assertEqual(expect.dataIn, out.dataIn)

if __name__ == '__main__':
    unittest.main()
