import unittest

class Animal:
    def __init__(self, nome , som):
        self.nome = nome
        self.som = som

    def falar(self):
        return 'O %s disse "%s"' % (self.nome, self.som)

class AnimalTestCase(unittest.TestCase):
    def setUp(self):
        self.leao = Animal(nome="leao", som="rugido")
        self.gato = Animal(nome="gato", som="miau")

    def testFala(self):
        self.assertEqual(self.leao.falar(), 'O leao disse "rugido"')
        self.failUnlessEqual(self.gato.falar(), 'O gato disse "miau"')

    def testFala2(self):
        self.assertEqual(self.leao.falar(), 'O leao disse "rugido"')
        self.assertEquals(self.gato.falar(), 'O gato disse "miau"')

class AnimalTestCase2(unittest.TestCase):
    def setUp(self):
        self.leao = Animal(nome="leao", som="rugido")
        self.gato = Animal(nome="gato", som="miau")

    def testFala(self):
        self.assertEquals(self.leao.falar(), 'O leao disse "rugido"')
        self.assertEquals(self.gato.falar(), 'O gato disse "miau"')

    def testFala2(self):
        self.assertEquals(self.leao.falar(), 'O leao disse "rugido"')
        self.assertEquals(self.gato.falar(), 'O gato disse "miauf"')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AnimalTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
#if __name__ == '__main__':
#    unittest.main()

