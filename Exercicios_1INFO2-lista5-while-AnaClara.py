# Lista de exercícios 5 - repetição com while

def quantidade_de_impares(valor_inicial, valor_final):
    ''' Determine a quantidade de números ímpares num intervalo'''
    impar = 0
    im =  valor_inicial + 1
    while im < valor_final:
        if im % 2 != 0:
            impar += 1
            im += 1
        else:
            im += 1
    return impar


def soma_dos_inteiros(valor1, valor2):
    ''' Calcule a soma dos números inteiros no intervalo entre 'valor1'
    e o 'valor2' ou vice-versa, considerando que podem ser informado
    números negativos ou fora de ordem. 
    Ex: 1 e 5 ou 5 e 1, retorna 9'''
    if valor1 > valor2:
        valour1 = valor2
        valour2 = valor1
    else:
        valour1 = valor1
        valour2 = valor2
    soma = 0
    num = valour1 + 1
    while num < valour2:
            soma += num
            num += 1
    return soma

def potencia(base, expoente):
    ''' Calcule a 'base' elevada ao 'expoente' manualmente sem usar 
    'base**expoente'. Considere base e expoente como inteiros positivos.'''
    if expoente == 0:
        return 1
    cont = 1
    num = base
    while cont < expoente:
        num = num * base
        cont += 1
    return num

def crescimento_populacional(populacao1, populacao2, crescimento1,
                             crescimento2):
    ''' Calcule quantos anos levará para a 'população1' ultrapassar a 
    'população2', baseado em suas porcentagens de crescimento.'''
    if populacao1 > populacao2:
        return 0
    if crescimento1 < crescimento2:
        return 0
    anos = 0
    while populacao1 < populacao2:
        pop1 = populacao1 * (crescimento1/100)
        populacao1 += pop1
        pop2 = populacao2 * (crescimento2/100)
        populacao2 += pop2
        anos += 1
    return anos


def Fibonacci(n):
    ''' Retorne o n-ésimo valor da série de Fibonacci
    Fibonacci = 1,1,2,3,5,8,13,...'''
    ant_1 = 1
    ant_2 = 0
    cont = 0
    while cont < n:
        soma = ant_1 + ant_2
        ant_1 = ant_2
        ant_2 = soma
        cont += 1
    return soma


def fatorial(numero):
    ''' Calcule e retorne o fatorial do 'numero' informado,
    O fatorial é o valor produtório dos valores menores ou iguais ao número
    ex: fatorial de 4 é 4*3*2*1 e retorna 24'''
    if numero == 0:
        return 1
    num_inicial = numero - 1
    fato = numero
    while num_inicial > 0:
        fato = fato * num_inicial 
        num_inicial = num_inicial - 1
    return fato

def é_primo(valor):
    ''' Verifique se o 'valor' informado é primo.
    Um número primo é aquele que é divisível apenas por ele mesmo e por 1'''
    if valor == 2:
        return True
    elif valor in (0,1) or valor % 2 == 0:
        return False
    for i in range(2, valor):
        if valor % i == 0:
            return False
    return True

def quantidade_de_primos(comeco, final):
    ''' Retorne a quantidade de primos entre os valores informados'''
    contador_de_primos = 0
    n = comeco + 1
    while n < final:
        if é_primo(n):
            contador_de_primos += 1
        n += 1
    return contador_de_primos
    

def lista_de_primos(inicio, fim):
    '''Retorne uma lista de primos entre os valores informados, incluindo
    os limites'''
    iniciou = inicio 
    finalizou = fim + 1
    lista_de_primoss = []
    while iniciou < finalizou:
        if é_primo(iniciou):
            lista_de_primoss.append(iniciou)
        iniciou += 1
    return lista_de_primoss

def serie1(n):
    '''Dado n, calcule o valor de
    s = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n '''
    num = 0
    divisor = 1
    while divisor <= n:
        num += 1/divisor
        divisor += 1
    return round(num,2)

def serie2(n):
    '''Dado n, calcule o valor de
    s = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m'''
    num = 0
    divisor_de_cima = 1
    divisor_c_soma_dois = 1
    o_q_conta_o_numero_n = 1
    while o_q_conta_o_numero_n <= n:
        num += divisor_de_cima / divisor_c_soma_dois
        divisor_de_cima += 1
        divisor_c_soma_dois += 2
        o_q_conta_o_numero_n +=1
    return round(num,2)


def serie_pi(n):
    ''' Calcule o valor de pi através da série
    4/1 - 4/3 + 4/5 - 4/7 + ... - 4/m, sendo informado
    o número n de iterações '''
    contador = 1
    m = 0
    divison = 1
    nao_sei= 1
    while contador <= n:
        if nao_sei % 2 == 0:
            m -= 4/divison
        else:
            m += 4/divison
        divison += 2
        nao_sei += 1
        contador += 1
    return round(m,6)

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' % ('Falhou')
    else:
        prefixo = '\033[32m%s' % ('Passou')
        acertos += 1
    print('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado),
                                                    repr(obtido)))


def main():
    print('Quantidade de ímpares:')
    test(quantidade_de_impares(1, 3), 0)
    test(quantidade_de_impares(1, 4), 1)
    test(quantidade_de_impares(1, 5), 1)
    test(quantidade_de_impares(1, 10), 4)
    test(quantidade_de_impares(1, 50), 24)
    test(quantidade_de_impares(1, 60), 29)
    test(quantidade_de_impares(40, 80), 20)

    print('Soma de números inteiros:')
    test(soma_dos_inteiros(1, 50), 1224)
    test(soma_dos_inteiros(50, 1), 1224)
    test(soma_dos_inteiros(10, 1), 44)
    test(soma_dos_inteiros(-10, 1), -45)
    test(soma_dos_inteiros(10, -10), 0)

    print('Potência:')
    test(potencia(2, 1), 2)
    test(potencia(2, 2), 4)
    test(potencia(1, 20000), 1)
    test(potencia(2, 4), 16)
    test(potencia(10000, 1), 10000)
    test(potencia(2, 10), 1024)
    test(potencia(2, 0), 1)
    test(potencia(10, 0), 1)

    print('Aumento da população:')
    test(crescimento_populacional(80000, 200000, 3, 1.5), 63)
    test(crescimento_populacional(2000, 2020, 1.1, 1), 11)
    test(crescimento_populacional(2000, 1000, 1.1, 1), 0)
    test(crescimento_populacional(1000, 2000, 1, 1.1), 0)

    print('Fibonnaci:')
    test(Fibonacci(1), 1)
    test(Fibonacci(2), 1)
    test(Fibonacci(3), 2)
    test(Fibonacci(4), 3)
    test(Fibonacci(5), 5)

    print('Fatorial:')
    test(fatorial(0), 1)
    test(fatorial(1), 1)
    test(fatorial(5), 120)
    test(fatorial(10), 3628800)

    print('Primo:')
    test(é_primo(0), False)
    test(é_primo(1), False)
    test(é_primo(2), True)
    test(é_primo(3), True)
    test(é_primo(4), False)
    test(é_primo(5), True)
    test(é_primo(7), True)
    test(é_primo(11), True)
    test(é_primo(121), False)
    test(é_primo(169), False)

    print('Quantidade de primos no intervalo:')
    test(quantidade_de_primos(5, 10), 1)
    test(quantidade_de_primos(10, 20), 4)
    test(quantidade_de_primos(0, 21), 8)
    test(quantidade_de_primos(43, 102), 12)

    print('Lista de primos:')
    test(lista_de_primos(0, 1), [])
    test(lista_de_primos(5, 10), [5, 7])
    test(lista_de_primos(10, 20), [11, 13, 17, 19])
    test(lista_de_primos(0, 21), [2, 3, 5, 7, 11, 13, 17, 19])
    test(lista_de_primos(43, 102), [43, 47, 53,
                                    59, 61, 67, 71, 73, 79, 83, 89, 97, 101])

    print('Série 1:')
    test(serie1(1), 1.00)
    test(serie1(15), 3.32)
    test(serie1(10), 2.93)
    test(serie1(5), 2.28)

    print('Série 2:')
    test(serie2(1), 1.00)
    test(serie2(2), 1.67)
    test(serie2(3), 2.27)
    test(serie2(4), 2.84)

    print('Série pi:')
    test(serie_pi(1), 4.000000)
    test(serie_pi(2), 2.666667)
    test(serie_pi(3), 3.466667)
    test(serie_pi(4), 2.895238)
    test(serie_pi(5), 3.339683)
    test(serie_pi(6), 2.976046)
    test(serie_pi(7), 3.283738)
    test(serie_pi(8), 3.017072)
    test(serie_pi(9), 3.252366)
    test(serie_pi(10), 3.041840)
    test(serie_pi(100), 3.131593)
    test(serie_pi(150), 3.134926)
    test(serie_pi(1000), 3.140593)
    test(serie_pi(5000), 3.141393)
    test(serie_pi(9000), 3.141482)


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total, acertos,
                                                        total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
