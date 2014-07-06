#! /usr/bin/python

def translate(text, num=2):
    l = list(text)
    ln = map(ord, l)
    #ln = map(lambda x: x + num, ln)
    for i in range(len(ln)):
        if ln[i] not in [ord('.'), ord('('), ord(')'), ord(' '), ord("'")]:
            if ln[i] not in [ord('y'), ord('z')]:
                ln[i] = ln[i] + num
            else:
                #conv = {ord('y'): ord('a'), ord('z'): ord('b')}
                #ln[i] = conv[ln[i]]
                ln[i] = ord('a') if ln[i] == ord('y') else ord('b')
    
    l = map(chr, ln)
    return ''.join(l)

def tr(text):
    import string
    tb = string.maketrans(string.lowercase, 
        string.lowercase[2:] + string.lowercase[:2])
    return string.translate(text, tb)

def trFromFile():
    txt = open('map.txt', 'r').read()
    return txt, tr(txt)

def translateFromFile():
    f = open('map.txt', 'r')
    txt = f.read()
    f.close()
    return txt, translate(txt)

def flow():
    l = [ord('('), ord(')')]
    if ord(')') not in l:
        print 'if'
    else: print 'else'

if __name__ == '__main__':
    print('tr: ',trFromFile(), '\n')
    print('tr in url: ',tr('map')) 

