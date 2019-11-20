import unittest

def limpador_de_cpf(cpf):
    '''limpa o cpf, transforma ele em int pah'''
    cpf_top = ''
    for i in cpf:
        if i.isdigit():
            cpf_top += i    
    return cpf_top


def checa_tamanho(cpf):
    '''vai checar o tamanho do cpf'''
    contador_de_numeros = 0
    a = limpador_de_cpf(cpf)
    for i in a:
        if i.isdigit():
            contador_de_numeros += 1
    if contador_de_numeros < 11:
        return False
    else:
        return True

def testa_cpf_finalmente(cpf):
    '''vai ver se o cpf e top'''
    pra_dar_a_soma = []
    b = checa_tamanho(cpf)
    if b == False:
        return False
    else:
        c = limpador_de_cpf(cpf)
        for i in c:
            if i.isdigit():
                d = int(i)
                pra_dar_a_soma.append(d)
        if sum(pra_dar_a_soma) % 11 == 0:
            return True
        else:
            return False
   

def testa_cpf_dnovo(cpf):
    '''outra forma de testar se o cpf e real'''
    j = checa_tamanho(cpf)
    pra_separar_os_nums = []
    if j == False:
        return False
    else:
        k = limpador_de_cpf(cpf)
        for i, p in k:
            if i >= 0 and i < 9:
                pp = int(p)
                pra_separar_os_nums.append(pp)
        q = pra_separar_os_nums[0] * 10
        w = pra_separar_os_nums[1] * 9
        e = pra_separar_os_nums[2] * 8
        r = pra_separar_os_nums[3] * 7
        t = pra_separar_os_nums[4] * 6
        y = pra_separar_os_nums[5] * 5
        u = pra_separar_os_nums[6] * 4
        l = pra_separar_os_nums[7] * 3
        m = pra_separar_os_nums[8] * 2
        aninha = (q + w + e + r + t + y + u + l + m) *



class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(limpador_de_cpf('116793229-32'), '11679322932')
        self.assertEqual(limpador_de_cpf('116794009-16'), '11679400916')

    def test(self):
        self.assertEqual(checa_tamanho('116793229-32'), True)
        self.assertEqual(checa_tamanho('116794009-16'), True)
        self.assertEqual(checa_tamanho('11'), False)

    def test(self):
        self.assertEqual(testa_cpf_finalmente('116793229-32'), False)
        self.assertEqual(testa_cpf_finalmente('116794009-16'), True)
        
if __name__ == '__main__':
    unittest.main()

 




