class CodeJam:
    '''
    CodeJam Workflow Integration
    Actualy works with input and output files
    '''
    def __init__(self, fname):
        self.fname = fname.split('.')[0]
        self.readIn(fname)
    
    def readIn(self, fname):
        self.dataIn = [l.replace('\n','') for l in open(fname,'r').readlines()]
    
    def writeOut(self, data):
        '''
        Logic class must call this method in end of the process.
        '''
        open(self.fname+'.out','w').writelines([l+'\n' for l in data])

class Words(CodeJam):
    '''
    Logic class to implement reverse words solution.
    '''
    
    def revert(self):
        if int(self.dataIn[0]) == len(self.dataIn)-1:
            data = [self.dataIn[i].split(' ') for i in range(1,len(self.dataIn))]
            for l in data: l.reverse()
            self.writeOut(['Case #%d: %s' % (i+1, ' '.join(data[i])) for i in range(len(data))])
        else: raise Exception('Lenght of data not is valid')

    def revertFunc(self):
        if int(self.dataIn[0]) == len(self.dataIn)-1:
            data2 = self.dataIn
            data2.pop(0)
            data = map(lambda l: l.split(' '), data2)
            map(lambda l: l.reverse(),data)
            self.writeOut(map(lambda i: 'Case #%d: %s' % (i+1, ' '.join(data[i])) ,range(len(data))))
        else: raise Exception('Lenght of data not is valid')

if __name__ == '__main__':
    import sys
    w = Words(sys.argv[1])
    w.revert()

