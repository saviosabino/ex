
def pingpong(number):
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

def printpng(number, info):
    ''' utility to print out'''
    print("%d: %s" % (number, info))

def sequence(number):
    count = 1
    while count <= number:
        yield count
        count += 1

def iterpng(turns):
    '''utility to iterate and return a list'''
    info_list = [pingpong(n) for n in sequence(turns)]
    return info_list

def iterprintpng(turns):
    '''
    This process and print the information
    in the same interation
    '''
    for number in sequence(turns):
        printpng(number, pingpong(number))

import unittest
class Test_pingpong(unittest.TestCase):
    def test_if_10_pong(self):
        self.assertEqual('pong', pingpong(10))

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        param = sys.argv[1]
        if param == 'test' or param == 't':
            unittest.main()
        else:
            try:
                turns = int(param)
            except:
                print('error, maybe you dont\' type a number')
            else:
                iterprintpng(turns)
    else:
        print('usage:')
        print('type "test" (t) to test the program')
        print('type a number of turns to repeat the pingpong')

