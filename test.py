import unittest

def testador_de_cpf(cpf):
    '''testa o cpf pra ve se é real
    o cpf vem em string'''
    cpfval = cpf.replace('-','')
    cpf_valido = [int(cpfval)]
    if len(cpf_valido) == 11:
        return True
    else:
        print(len(cpf_valido))
        return False
   


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(testador_de_cpf('116793229-32'), False)
        self.assertEqual(testador_de_cpf('116794009-16'), True)
        self.assertEqual(testador_de_cpf('11679322931'), True)
        self.assertEqual(testador_de_cpf('11'), False)
        
if __name__ == '__main__':
    unitest.main()