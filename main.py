""""""""
from random import randint
from time import sleep


def jogo_de_dados(*args):
    score_dado1 = 0
    score_dado2 = 0
    while True:
        dado1 = randint(1, 6)
        dado2 = randint(1, 6)
        print('Se caso nao quiser jogar, digite o numero 3!!!')
        escolha = int(input('Informe qual dado voce escolhe, dado 1 ou dado 2: '))
        if escolha == 1:
            print('Dado 1 escolhido!!!')
            print('Preparando para jogar!!!')
            print('*************************')
            sleep(2)
            if dado1 > dado2:
                print(f'Voce ganhou, o dado 1 teve o maior numero [Dado 1: {dado1}] > [Dado 2: {dado2}]')
                score_dado1 += 1
            elif dado1 == dado2:
                print(f'EMPATE, os dados tiveram o mesmo resultado [Dado 1: {dado1}] = [Dado 2: {dado2}]')
            else:
                print(f'Voce perdeu, o dado 2 teve o maior numero [Dado 1: {dado1}] < [Dado 2: {dado2}]')
                score_dado2 += 1
        elif escolha == 2:
            print('Dado 2 escolhido!!!')
            print('Preparando para jogar!!!')
            print('*************************')
            sleep(2)
            if dado1 < dado2:
                print(f'Voce ganhou, o dado 2 teve o maior numero [Dado 2: {dado2}] > [Dado 1: {dado1}]')
                score_dado2 += 1
            elif dado1 == dado2:
                print(f'EMPATE, os dados tiveram o mesmo resultado [Dado 2: {dado2}] = [Dado 1: {dado1}]')
            else:
                print(f'Voce perdeu, o dado 2 teve o maior numero [Dado 2: {dado2}] < [Dado 1: {dado1}]')
                score_dado1 += 1
        elif escolha == 3:
            print('PROGRAMA ENCERRADO')
            print('*************************')
            print(f'O dado 1 teve [{score_dado1}] pontos')
            print(f'O dado 2 teve [{score_dado2}] pontos')
            break
        else:
            print('ESCOLHA ENTRE AS OPCOES, 1, 2 ou 3!!!')
            escolha = int(input('Informe qual dado voce escolhe, dado 1 ou dado 2: '))


jogo_de_dados()


