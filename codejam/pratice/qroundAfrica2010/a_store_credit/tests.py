import unittest
import logic

class TestLogic(unittest.TestCase):
    def cttestOrganize(self):
        cs = logic.CreditStore('test.in')
        cs.chooseItems()
        #expect = logic.CodeJam('expect.out')
        #out = logic.CodeJam('test.out')
        self.assertEqual(50, len(cs.data))
    
    def testOutput(self):
        cs = logic.CreditStore('test.in')
        cs.chooseItems()
        expect = logic.CodeJam('expect.out')
        out = logic.CodeJam('test.out')
        self.assertEqual(expect.dataIn, out.dataIn)

if __name__ == '__main__':
    unittest.main()
