def printNum(x):
    for i in range(1,x+1):
        print logicNum(i)

def logicNum(x,pref='ping'):
    if x % 3 == 0:
        if pref == 'pong' and x % 5 == 0:
             return 'pong'
        return 'ping'
    elif x % 5 == 0: return 'pong'
    else: return x

if __name__ == '__main__':
    import sys
    printNum(int(sys.argv[1]))
