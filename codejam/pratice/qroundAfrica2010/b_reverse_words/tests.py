import unittest
import logic

class TestLogic(unittest.TestCase):
    def testInvert(self):
        w = logic.Words('test.in')
        w.revertFunc()
        expect = logic.CodeJam('expect.out')
        out = logic.CodeJam('test.out')
        self.assertEqual(expect.dataIn, out.dataIn)

if __name__ == '__main__':
    unittest.main()