#!/usr/bin/env python
# coding: utf-8

from minimongo import *

class A(Model):
    class Meta:
        database = 'mDB'

    
    def __init__(self, *args, **kwargs):
    #metodo apenas para informar o padrão do schema e 
    #pre popular para testes
        #a = A()
        self.x=1
        self.y=2
        self.z=3
        self.b = B()
        super(Model,self).__init__(*args, **kwargs)

class B(Model):
    class Meta:
        database = 'mDB'

    #def __init__(self):
    #    self.i=10
    #    self.j=20
    #    self.a = A()

