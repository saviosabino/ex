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
        
    def run(self):
        raise Exception("implementThis")


class BotTrust(CodeJam):
    #Logic class
    def organizeData(self):
        self.data = []
        self.dataRet = []
        
    def startCase(self, instruction):
        self.seconds = 0
        self.instruction = instruction
        self.currentMatch = 0
        
        self.Orange = Bot("Orange")
        self.Blue = Bot('Bue')
        
        
    def solveCase(self):
        curInstruction = self.instruction[self.currentMatch]
        
    
    def run(self):
        pass
        

class Bot:
    def __init__(self, name):
        self.name = name
        self.position = 1
    
    def move(self, position):
        self.position = position
    
    def pushButton(self):
        pass

class Hallway:
    def __init__(self):
        self.buttons = range(1, 100+1)


        
        

if __name__ == '__main__':
    import sys
    l = BotTrust(sys.argv[1])
    l.defLogic()


