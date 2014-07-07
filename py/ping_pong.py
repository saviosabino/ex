class PingPong:

    def __init__(self, turns):
        self.sequence = self.set_sequence(turns)
        self.turns = turns

    def logic(self, number):
        """function that print: 
        ping if n is divisible by 2
        pong if n is divisible by 3
        n if not divisible by 2 or 3
        the ping and pong must be cumulative.
        """
        info = '' #string that cumulate the data to print
        
        if number % 2 == 0 and number % 3 != 0: 
            info = 'ping'
        elif number % 3 == 0: 
            if number % 2 != 0:
                info += 'pong'
            else: info += 'ping, pong'
        else: info = number

        return info

    def printpng(self, number, info):
        ''' utility to print out'''
        print("%d: %s" % (number, info))

    def set_sequence(self, turns):
        count = 1
        while count <= turns:
            yield count
            count += 1

    def reset_sequence(self, turns):
        turns = turns if turns else self.turns
        self.sequence = set_sequence(turns)

    def iterprintpng(self):
        '''
        This process and print the information
        in the same interation
        '''
        for number in self.sequence:
            self.printpng(number, self.logic(number))

import unittest
class TestPingpong(unittest.TestCase):

    def setUp(self):
        self.pg = PingPong(10)

    def test_if_5_is_5(self):
        self.assertEqual(5, self.pg.logic(5))

    def test_if_10_ping(self):
        self.assertEqual('ping', self.pg.logic(10))

    def test_if_6_ping_and_pong(self):
        self.assertEqual('ping, pong', self.pg.logic(6))

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        param = sys.argv[1]
        if param == '--test' or param == '-t':
            loadTest = unittest.TestLoader().loadTestsFromTestCase
            suite = loadTest(TestPingpong)
            unittest.TextTestRunner(verbosity=2).run(suite)
        else:
            try:
                turns = int(param)
            except:
                print('error, maybe you dont\' type a number')
            else:
                pg = PingPong(turns)
                pg.iterprintpng()
    else:
        print('usage:')
        print('type "test" (t) to test the program')
        print('type a number of turns to repeat the pingpong')

