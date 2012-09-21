class CodeJam:
    '''
    CodeJam Workflow Integration
    Actualy works with input and output files
    '''
    def __init__(self, fname):
        self.fname = fname.split('.')[0]
        self.readIn(fname)
    
    def readIn(self, fname):
        self.dataIn = [l.replace('\n','').replace('\r','') for l in open(fname,'r').readlines()]
    
    def writeOut(self, data):
        '''
        Logic class must call this method in end of the process.
        '''
        open(self.fname+'.out','w').writelines([l+'\n' for l in data])


class T9(CodeJam):
    #Logic Class
    def __init__(self, fname):
        CodeJam.__init__(self,fname)
        self.nMap={0:[' ',], 1: [], 2:['a','b','c'], 3:['d','e','f'],
            4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'],
            7:['p','q','r','s'], 8:['t','u','v'], 9: ['w','x','y','z']}
        self.lMap={'a':2,'b':2,'c':2,'d':3,'e':3,'f':3,'g':4,'h':4,'i':4,
            'j':5,'k':5,'l':5,'m':6,'n':6,'o':6,'p':7,'q':7,'r':7,'s':7,
            't':8,'u':8,'v':8,'w':9,'x':9,'y':9,'z':9,' ':0}
    
    def writeN(self):
        nM,lM = self.nMap, self.lMap
        if int(self.dataIn[0]) == len(self.dataIn)-1:
            self.dataIn.pop(0)
            data=[]
            for lSeq in self.dataIn:
                nSeq = ''
                lAnt = ''
                for lDig in lSeq:
                    nDig = str(lM[lDig]) * (nM[lM[lDig]].index(lDig)+1)
                    if nDig[0] != lAnt: nSeq += nDig
                    else: nSeq += ' ' + nDig
                    lAnt = nDig[0]
                data.append(nSeq)
            self.writeOut(['Case #%d: %s' % (i+1, ''.join(data[i])) for i in range(len(data))])
        else: raise Exception('Lenght of data not is valid')

    
if __name__ == '__main__':
    import sys
    t9 = T9(sys.argv[1])
    t9.writeN()

