import os

print('dirname: ' + os.path.dirname(__file__))
print('realpath: ' + os.path.realpath(os.path.dirname(__file__)))
print('__file__: ' + __file__)
print('dir(): ' + str(dir()))

