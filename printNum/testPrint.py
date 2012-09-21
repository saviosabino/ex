import printNum
import unittest

class TestNum(unittest.TestCase):
    '''
    imprimir 1 a 100
    mult 3 ping
    mult 5 pong
    '''
    def testPrint(self):
        print '\ntestPrint:'
        printNum.printNum(100)
    
    def test1e1(self):
        self.assertEqual(1,printNum.logicNum(1))
    
    def test2e2(self):
        self.assertEqual(2,printNum.logicNum(2)) 
    
    def test3ePing(self):
        self.assertEqual('ping',printNum.logicNum(3))
    
    def test10ePong(self):
        self.assertEqual('pong',printNum.logicNum(10)) 
    
    def testPings0a100(self):
        print '\ntestPings:'
        for i in range(1, 100+1):
            if i % 3 == 0:
                self.assertEqual('ping',printNum.logicNum(i))
                print 'ping: %d' % i
                continue

    def testPongs0a100(self):
        print '\ntestPongs:'
        for i in range(1, 100+1):
            if i % 5 == 0:
                self.assertEqual('pong',printNum.logicNum(i,'pong'))
                print 'pong: %d' % i
                continue

    def testNPings0a100(self):
        print '\ntestNPings:'
        for i in range(1, 100+1):
            if i % 3 != 0:
                self.assertNotEqual('ping',printNum.logicNum(i))
                print'nPing: %d' % i
                continue

    def testNPongs0a100(self):
        print '\ntestNPongs:'
        for i in range(1,100+1):
            if i % 5 != 0:
                self.assertNotEqual('pong',printNum.logicNum(i,'pong'))
                print 'nPong: %d' %i
                continue

if __name__ == '__main__':
    unittest.main()

