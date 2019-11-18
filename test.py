import unittest

def limpador_de_cpf(cpf):
    '''limpa o cpf, transforma ele em int pah'''
    cpf_top = ''
    for i in cpf:
        if i.isdigit():
            cpf_top += i    


def testa_cpf(cpf):
    '''vai ver se o cpf e real'''
    cpf_cool = limpador_de_cpf(cpf)
    if cpf_cool == True:
            if len(cpf_cool) == 11:
                bb = int(cpf_cool)
                if sum(bb) % 11 == 0:
                    return True
    else:
        return False






class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(testa_cpf('116793229-32'), False)
        self.assertEqual(testa_cpf('116794009-16'), True)
        
if __name__ == '__main__':
    unittest.main()