import unittest
import logic

class TestLogic(unittest.TestCase):
    
    
    def testOutput(self):
        l = logic.BotTrust('test.in')
        l.run()
        expect = logic.CodeJam('expect.out')
        out = logic.CodeJam('test.out')
        self.assertEqual(expect.dataIn, out.dataIn)

if __name__ == '__main__':
    unittest.main()
