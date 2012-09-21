
def multi(vals):
    """
    multi de valores
    qtde. indefinida
    depende de uma lista
    como parametro
    """
    res=1
    for v in vals: res = res * v
    return res

if __name__ == '__main__':
    lista=[]
    a=1
    while a != 's':
        a=input('dig. um numero, s para sair:')
        if isinstance(a,(int,float)): lista.append(a)
    print multi(lista)
    print 'doc de multi: %s' % multi.__doc__

