 
from random import randint
dado1=randint(1,6)
print("Dado 1=",dado1)
dado2=randint(1,6)
print("Dado 2=",dado2)
dado3=randint(1,6)
print("Dado 3=",dado3)
dado4=randint(1,6)
print("Dado 4=",dado4)
soma_dados=dado1+dado2
print("Soma dos dados 1 e 2=",soma_dados)
soma_dados2=dado3+dado4
print("Soma dos dados 3 e 4=",soma_dados2)
if soma_dados>soma_dados2:
    print("Jogador 1 venceu!")
elif soma_dados2>soma_dados:
    print("Jogador 2 venceu!")
elif soma_dados==soma_dados2:
        print("Empate")
