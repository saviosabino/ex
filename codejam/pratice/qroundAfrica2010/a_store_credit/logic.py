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


class CreditStore(CodeJam):
    #Logic class
    def organizeData(self):
        self.data =[]
        for i in range(int(self.dataIn[0])):
            self.data.append([self.dataIn[i*3+1],
                self.dataIn[i*3+2],self.dataIn[i*3+3]])
        for l in self.data: 
            l[0] = int(l[0])
            l[1] = int(l[1])
            l[2] = l[2].split(' ')
            for i in range(len(l[2])): l[2][i] = int(l[2][i])
        
    def chooseItems(self):
        self.organizeData()
        #a=1
	    #print self.data
        for line in self.data: 
            #print a
            #a+=1
            for i in range(len(line[2])):
                jv = line[0] - line[2][i]
                hasJv = line[2].count(jv)
                if hasJv:
                    j = line[2].index(line[0] - line[2][i])
                    if j == i and line[2].count(line[0] - line[2][i]) > 1: 
			            j = line[2].index(line[0] - line[2][i],i+1)
                    if i < j: line.append([i+1,j+1])
              
        self.writeOut(['Case #%d: %d %d' % (i+1,self.data[i][3][0],\
            self.data[i][3][1]) for i in range(len(self.data))])


    def chooseItemsSlow(self):
        self.organizeData()
        for line in self.data:
            for i in range(len(line[2])):
                for j in range(len(line[2])):
                    if i != j and line[2][i] + line[2][j] == line[0]:
                        line.append([i+1,j+1])
        self.writeOut(['Case #%d: %d %d' % (i+1,self.data[i][3][0],\
            self.data[i][3][1]) for i in range(len(self.data))])
	
if __name__ == '__main__':
    import sys
    cs = CreditStore(sys.argv[1])
    cs.chooseItems()

