"""
#1
nota = float(input('Digite uma nota entre 0 e 10: '))

while True:
    if nota > 10:
        nota = float(input('Digite uma nota entre 0 e 10: '))
    elif nota < 0:
        nota = float(input('Digite uma nota entre 0 e 10: '))
    else:
        print(f'CORRETO!!! {nota}')
        break




#2
usuario = input('Informe o nome de seu usuario: ')
senha = input('Informe a senha de seu usuario: ')

while True:
    if usuario == senha:
        print('USUARIO E SENHA NAO PODEM SER IGUAIS, MUDE UM DOS DOIS!!!')
        usuario = input('Informe o nome de seu usuario: ')
        senha = input('Informe a senha de seu usuario: ')
    else:
        print('Usuario e senha computados com sucesso!')
        break




#3
nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))
salario = float(input('Informe seu salario: '))
sexo = input('Informe seu sexo: ')
sexos_op = ['m', 'f', 'M', 'F']
estado_civil = input('Informe seu estado civil: ')
estados_op = ['s', 'S', 'c', 'C', 'v', 'V', 'd', 'D']

while True:
    if len(nome) < 3:
        print('Nome deve conter mais de tres caracteres!')
        nome = input('Informe seu nome: ')
    elif idade < 0 and idade > 150:
        print('Idade deve ser maior que 0 e menor quero 150!')
        idade = int(input('Informe sua idade: '))
    elif  not sexo in sexos_op:
        print('Informe o sexo corretamente, M (Masculino) ou F (Feminino)!')
        sexo = input('Informe seu sexo: ')
    elif salario < 0:
        print('Informe um salario maior que 0!')
        salario = float(input('Informe seu salario: '))
    elif not estado_civil in estados_op:
        print('Informe o estado civil corretamente, s (Solteiro[a]), c (Casado[a]), v (Viuvo[a]) e d (Divorciado[a])')
        estado_civil = input('Informe seu estado civil: ')
    else:
        print('Informacoes computadas com sucesso!')
        break

print(nome)
print(idade)
print(salario)
print(sexo)
print(estado_civil)




#4
populacao_a = 80000
populacao_b = 200000
anos = 0

while populacao_a < populacao_b:
    populacao_a += populacao_a * 0.03
    populacao_b += populacao_b * 0.015
    anos += 1

print(f'Demoraram {anos} anos para populacao A crescendo 3% ao ano passar a populacao B que crescia 1,5% ao ano tambem!')
print(f'A populacao A ficou com ({round(populacao_a, 1)}) habitantes e a populacao B ficou com ({round(populacao_b, 1)}) habitantes')




#5
populacao_a = int(input('Informe o numero de habitantes da cidade A: '))
populacao_b = int(input('Informe o numero de habitantes da cidade B: '))
taxa_cres_A = float(input('Informe a taxa de crescimento da populacao A: '))
taxa_cres_B = float(input('Informe a taxa de crescimento da populacao B: '))
anos = 0

while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_cres_A
    populacao_b += populacao_b * taxa_cres_B
    anos += 1

print(f'Demoraram {anos} anos para populacao A crescendo 3% ao ano passar a populacao B que crescia 1,5% ao ano tambem!')
print(f'A populacao A ficou com ({round(populacao_a, 1)}) habitantes e a populacao B ficou com ({round(populacao_b, 1)}) habitantes')




#6
for n in range(1, 21):
    print(n, end=' ')




#7
a = 0
lista = []
for i in range(1, 6):
    a += 1
    num = int(input(f'Informe o {a} numero: '))
    lista.append(num)


print(f'O maior numero informado eh {max(lista)}')




#8
lista = []
for i in range(1, 6):
    num = int(input('Informe um numero: '))
    lista.append(num)

print(f'A soma dos numeros eh: [{sum(lista)}]')
print(f'A media dos numeros eh: [{sum(lista) / 5}]')




#9
for i in range(1, 51, 2):
    print(i, end=' ')




#10
n1 = int(input('Informe um numero inteiro: '))
n2 = int(input('Informe um numero inteiro: '))

for i in range(n1+1, n2):
    print(i)




#11
n1 = int(input('Informe um numero inteiro: '))
n2 = int(input('Informe um numero inteiro: '))
lista = []

for i in range(n1, n2):
    lista.append(i)


print(sum(lista))




#12
num = int(input('Escolha um numero de 0 a 10 para fazer a tabuada: '))

for i in range(0, 10):
    i += 1
    resul = num * i
    print(f'[{num}] X [{i}] = [{resul}]')




#13
n1 = int(input('Informe o numero da base: '))
n2 = int(input('Informe o numero do expoente: '))

soma = n1 ** n2

print(soma)
print(pow(n1, n2))




#14
a = 0
numero_par = 0
numero_impar = 0
for i in range(1, 11):
    a += 1
    num = int(input(f'Informe o {a}º numero: '))

    if num % 2 == 0:
        numero_par += 1
    else:
        numero_impar += 1

print(f'A quantidade de numeros pares eh [{numero_par}]')
print(f'A quantidade de numeros impares eh [{numero_impar}]')




#15
def fibonacci(n):
    fib_series = []
    a, b = 1, 1
    for i in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Solicitar o valor de n ao usuário
n = int(input("Digite o valor de n para gerar a série de Fibonacci: "))

# Verificar se n é válido
if n <= 0:
    print("Digite um valor válido para n (maior que 0).")
else:
    result = fibonacci(n)
    print("Série de Fibonacci até o", n, "º termo:", result)




#16
def fibonacci():
    fib_series = [0, 1]
    while True:
        next_term = fib_series[-1] + fib_series[-2]
        if next_term > 500:
            break
        fib_series.append(next_term)
    return fib_series

# Chama a função para gerar a série
result = fibonacci()

print(result)




#17
num = int(input('Informe um numero para ser calculado o seu fatorial: '))
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i

print(fatorial)




#18
from random import *
num = int(input('Informe quantos numeros aleatorios o programa deve rodar: '))
lista = []

for i in range(1, num + 1):
    lista.append(randint(1, 100000))

print(f'Os numeros aleatorios sao [{lista}]')
print(f'O menor numero gerado aleatoriamente eh [{min(lista)}]')
print(f'O maior numero gerado aleatoriamente eh [{max(lista)}]')
print(f'A soma dos numeros gerados aleatoriamente eh [{sum(lista)}]')




#19
from random import *
num = int(input('Informe quantos numeros aleatorios o programa deve rodar: '))
lista = []

for i in range(1, num + 1):
    lista.append(randint(0, 1000))

print(f'Os numeros aleatorios sao [{lista}]')
print(f'O menor numero gerado aleatoriamente eh [{min(lista)}]')
print(f'O maior numero gerado aleatoriamente eh [{max(lista)}]')
print(f'A soma dos numeros gerados aleatoriamente eh [{sum(lista)}]')




#20
def calcula_fatorial(a):
    fatorial = 1
    soma = 0
    if num > 16:
        print('INFORME UM NUMERO MENOR QUE 16!!!')
    elif num < 0:
        print('INFORME UM NUMERO MAIOR QUE 0!!!')
    else:
        for i in range(1, num + 1):
            fatorial *= i
            soma = fatorial * vezes
    print(f'O calculo fatorial incial eh de [{fatorial}]')
    print(f'O calculo fatorial inicia multiplicado por ele mesmo [{vezes}] vezes resulta em [{soma}]')



num = int(input('Informe um numero menor que 16 para ser calculado o seu fatorial: '))
vezes = int(input('Informe quantas vezes calcular o fatorial: '))
calcula_fatorial(num)




#21
num = int(input('Informe um ate que numero ira ser checado se eh primo ou nao: '))
mult = 0

for i in range(1, num+1):
    if (num % i == 0):
        print(f'Multiplo de {i}')
        mult += 1

if (mult == 0):
    print('Eh primo')
else:
    print(f'Tem {mult} multiplos acima de 2 e abaixo de {num}')




#23
def eh_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True

    if numero % 2 == 0 or numero % 3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True


def encontrar_primos(N):
    primos = []
    divisoes = 0
    for numero in range(1, N + 1):
        divisoes += 1
        if eh_primo(numero):
            primos.append(numero)

    return primos, divisoes


try:
    N = int(input("Digite um número inteiro N: "))

    if N < 1:
        print("N deve ser maior ou igual a 1.")
    else:
        primos, divisoes = encontrar_primos(N)
        print(f"Números primos entre 1 e {N}: {primos}")
        print(f"Número de divisões realizadas: {divisoes}")
except ValueError:
    print("Por favor, insira um número inteiro válido.")




#24
from random import randint
num = int(input('Informe quantos aleatorios devem ser gerados e somados para ser calculado a media aritimetica deles: '))
soma = 0
lista = []

for i in range(1, num + 1):
    soma += randint(1, 1000)
    lista.append(soma)

soma = soma / num

print(f'Os numeros gerados aleatoriamente foram: [{lista}] e a media aritimetica eh: [{soma}]')




#Codigo pro meu amor
femea = input('Quem eh a namorada de Nicolas Braga Bastos: ')

while True:
    if femea != 'daniela':
        print('ERRADOOO, INSIRA O NOME DO AMOR DA VIDA DE NICOLAS BRAGA BASTOS')
        print('\U0001F621' * 10)
        femea = input('Quem eh o amor da vida de Nicolas Braga Bastos: ')

    else:
       print('Exatamente, Dani a mulher mais linda do mundo!!!')
       print('\U0001F60D' * 10)
       break




#jogo de dados
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




#25
from random import randint

escolha = int(input('Informe quantas pessoas devem participar da pesquisa: '))
lista = []
soma = 0
media = 0

for i in range(1, escolha + 1):
    i = randint(0, 100)
    lista.append(i)
    soma += i

media = soma / escolha
if media <= 25:
    idade = 'turma jovem'
elif media <= 60:
    idade = 'turma adulta'
elif media > 61:
    idade = 'turma idosa'

print(f'As pessoas entrevistadas tinham as seguintes idades: {lista}')
print('***************************************************************')
print(f'A media da idade das pessoas entrevistadas eh [{media}] anos')
print(f'Com base na media da idade das pessoas, chegou-se a conclusao que a turma eh uma [{idade}]')




#26
import random

candidato1 = 0
candidato2 = 0
candidato3 = 0

eleitores = int(input('Informe quantos eleitores vao participar da eleicao: '))

for i in range(1, eleitores + 1):
    voto = random.randint(1, 3)
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    else:
        candidato3 += 1

print('As eleicoes terminaram e os candidatos terminaram com essa quantidade de votos!')
print(f'Candidato 1 [{candidato1}]')
print(f'Candidato 2 [{candidato2}]')
print(f'Candidato 3 [{candidato3}]')

if candidato1 > candidato2 and candidato3:
    print(f'Candidato 1 foi eleito com [{candidato1}]')
elif candidato2 > candidato1 and candidato3:
    print(f'Candidato 2 foi eleito com [{candidato2}]')
elif candidato3 > candidato1 and candidato2:
    print(f'Candidato 3 foi eleito com [{candidato3}]')




#27
# Solicita a quantidade de turmas
num_turmas = int(input("Digite a quantidade de turmas: "))

total_alunos = 0  # Inicializa o total de alunos

# Loop para obter a quantidade de alunos em cada turma
for i in range(1, num_turmas + 1):
    while True:
        alunos_turma = int(input(f"Digite a quantidade de alunos da turma {i}: "))
        if 1 <= alunos_turma <= 40:  # Verifica se a quantidade de alunos está dentro do intervalo permitido
            total_alunos += alunos_turma
            break
        else:
            print("A quantidade de alunos deve estar entre 1 e 40.")

# Calcula o número médio de alunos por turma
media_alunos = total_alunos / num_turmas

print(f"O número médio de alunos por turma é: {media_alunos:.2f}")




#28
from random import randint
quantidades_cds = int(input('Informe quantos CDs o colecionador possue: '))
valor_cd = 0

for i in range(1, quantidades_cds + 1):
    valor_cd += randint(1, 1000)

print(f'O valor total gasto pelo o colecionador eh de [{valor_cd}]')
print(f'E o valor medio gasto em cada um deles eh de [{valor_cd / quantidades_cds}]')



Exercicios Classes
#1
class Bola:

    def __init__(self, cor: str, circunferencia: int, material: str):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material

    def trocaCor(self,nova_Cor: str):
        self.__cor = nova_Cor

    def mostraCor(self):
        return self.__cor

    def mostraCircunferencia(self):
        return self.__circunferencia

    def mostraMaterial(self):
        return self.__material

bola = Bola('Azul', 50, 'plastico')

print(bola.mostraCor())
print(bola.mostraMaterial())
print(bola.mostraCircunferencia())

bola.trocaCor('Vermelho')
print(bola.mostraCor())




#2
class Quadrado:

    def __init__(self, tamanhodoLado: int):
        self.__tamanhodoLado = tamanhodoLado

    def mudaLados(self,novosLados):
        self.__tamanhodoLado = novosLados
        return self.__tamanhodoLado

    def mostraLado(self):
        return self.__tamanhodoLado

    def calculaArea(self):
        return self.__tamanhodoLado * self.__tamanhodoLado







#3
class Retangulo(Quadrado):

    def __init__(self: object, ladoA: int, ladoB: int):
        self.__ladoA = ladoA
        self.__ladoB = ladoB

    def mudaLados(self: object,novoladoA: int, novoladoB: int):
        self.__ladoA = novoladoA
        self.__ladoB = novoladoB

    def mostraLado(self):
        return self.__ladoA
        return self.__ladoB

    def calculaArea(self):
        return self.__ladoA * self.__ladoB

    def calculaPerimetro(self):
        return self.__ladoA + self.__ladoB * 2





piso = 0.4
rodape = 0.1
medidaA = int(input('Informe a primeira medida do local: '))
medidaB = int(input('Informe a segunda medida do local: '))
piso_ao_quadrado = piso * piso
local = Retangulo(medidaA, medidaB)

calcula_local = medidaA * medidaB / piso_ao_quadrado

print(f'Vao ser necessarios [{calcula_local}] pisos')
"""



#4
import request


if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)

    print(requisicao)

    dic_requisicao = requisicao.json()

    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    bairro = dic_requisicao['bairro']
    print(dic_requisicao)
else:
    print("CEP Inválido")














































