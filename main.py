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




#4
class Pessoa:

    def __init__(self: object, nome: str, idade: int, peso: float, altura: int):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura


    def envelhecer(self, anos: int):
        self.__idade += anos
        anos *= 0.5
        self.__altura += anos

    def engordar(self, kilos):
        self.__peso += kilos

    def emagrecer(self, kilos):
        self.__peso -= kilos

    def crescer(self, centimetros):
        self.__altura += centimetros

    def mostrarNome(self):
        return self.__nome

    def mostraIdade(self):
        return self.__idade

    def mostraPeso(self):
        return self.__peso

    def mostraAltura(self):
        return self.__altura

    def mostraTudo(self):
        return f'Nome: {self.__nome} | Idade: {self.__idade} anos | Peso: {self.__peso}kg | Altura: {self.__altura}cm'




#5
class ContaCorrente:

    contas = {}

    def __init__(self: object, numeroConta: int, nomeCorrentista: str, saldo: float = 0):
        self.__numeroConta = numeroConta
        self.__nomeCorrentista = nomeCorrentista
        self.__saldo = saldo
        ContaCorrente.contas[numeroConta] = self

    def alterarNome(self: object, novoNome: str):
        self.__nomeCorrentista = novoNome

    def deposito(self: object, numeroContaDestino: int, valor: float):
        if valor > 0:
            numeroContaDestino = ContaCorrente.contas.get(numeroContaDestino)
            if numeroContaDestino:
                numeroContaDestino.__saldo += valor
                self.__saldo -= valor
            else:
                print(f'O numero da conta [{numeroContaDestino}] nao existe.')
        else:
            print('O valor do deposito deve ser maior que zero.')


    def saque(self: object, valor: float):
        if valor > 0:
            if self.__saldo > valor:
                self.__saldo -= valor
            else:
                print('O correntista nao possui o saldo para efetuar o saque!')
        else:
            print('Informe um valor maior que zero.')

    def mostrarConta(self: object):
        return f'Numero da conta: {self.__numeroConta} | Nome do correntista: {self.__nomeCorrentista} | Saldo: {self.__saldo}'

conta1 = ContaCorrente(1234567, 'Nicolas', 2300.50)
conta2 = ContaCorrente(7654321, 'Vanderlei', 70000.50)

conta1.deposito(7654321, 1000.50)
print(conta1.mostrarConta())
print(conta2.mostrarConta())




#6
class Tv:

    def __init__(self: object, canal: int, volume: int ):
        self.__canal = canal
        self.__volume = volume


    def mudaCanal(self: object, novoCanal: int):
        if novoCanal > 0:
            if novoCanal < 100:
                self.__canal = novoCanal
            else:
                print(f'Canal [{novoCanal}] nao disponivel')
        else:
            print(f'Informe um canal valido (de 0 a 100)')

    def mudaVolume(self: object, novoVolume):
        if novoVolume > 0:
            if novoVolume < 100:
                self.__canal = novoVolume
            else:
                print(f'Volume nao dispoviel, informe um volume valido (0 a 100)')
        else:
            print(f'Informe um volume valido (0 a 100)')

tv = Tv(40, 100)

tv.mudaCanal(1000)




#7
class BichinhoVirtual:


    def __init__(self: object, nome: str, satisfacao: int = 0, saude: int = 0, idade: int = 0): # Bug nesta linha, parametro idade nao pode ser obrigatorio
        self.__nome = nome
        self.__satisfacao = satisfacao
        self.__saude = saude
        self.__idade = idade

    def alterarNome(self: object, nome: str):
        self.__nome = nome

    def mostraNome(self):
        return self.__nome

    def alterarFome(self: object, satisfacao: int):
        self.__satisfacao = satisfacao

    def mostraFome(self):
        return self.__satisfacao

    def alterarSaude(self: object, saude: int):
        self.__saude = saude

    def mostraSaude(self):
        return self.__saude

    def alterarIdade(self: object, idade: int):
        self.__idade = idade

    def mostraIdade(self: object):
        return self.__idade

    def mostraHumor(self):
        if self.__satisfacao + self.__saude >= 180:
            print(f'O Tamagushi esta MUITO feliz {'\U0001F604'}')
            print(f'Ele esta com o humor de [{(self.__satisfacao + self.__saude) / 2}]')
        elif self.__satisfacao + self.__saude >= 150:
            print(f'O Tamagushi esta feliz {'\U0001F60A'}')
            print(f'Ele esta com o humor de [{(self.__satisfacao + self.__saude) / 2}]')
        elif self.__satisfacao + self.__saude >= 100:
            print(f'O Tamagushi nao esta nem triste e nem feliz {'\U0001F610'}')
            print(f'Ele esta com o humor de [{(self.__satisfacao + self.__saude) / 2}]')
        elif self.__satisfacao + self.__saude >= 50:
            print(f'O Tamagushi esta triste {'\U0001F641'}')
            print(f'Ele esta com o humor de [{(self.__satisfacao + self.__saude) / 2}]')
        elif self.__satisfacao + self.__saude >= 0:
            print(f'O Tamagushi esta MUITO triste {'\U0001F62D'}')
            print(f'Ele esta com o humor de [{(self.__satisfacao + self.__saude) / 2}]')
        else:
            print('Valores citados incompativeis!!!')

    def mostraTudo(self: object):
        print(f'O nome do Tamagushi eh {self.__nome}')
        print(f'O/A {self.__nome} esta [{self.__satisfacao}%] satisfeito')
        print(f'O/A {self.__nome} esta [{self.__saude}%] saudavel')
        print(f'O/A {self.__nome} tem [{self.__idade}] anos')



bicho = BichinhoVirtual('perola', 50, 50, 10)

bicho.mostraTudo()
bicho.mostraHumor()




#8
class Macaco:


    def __init__(self: object, nome: str):
        self.__nome = nome
        self.__bucho = []

    def comer(self: object, comida: str):
        if comida != ['macaco', 'Macaco', 'MACACO']:
            self.__bucho.append(comida)
        else:
            print('Macacos nao sao canibais!')

    def verBucho(self: object):
        return f'O bucho do macaco contem {self.__bucho}'

    def digerir(self: object):
        self.__bucho.clear()




#9
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f'Ponto: ({self.x}, {self.y})')


class Retangulo:
    def __init__(self, largura, altura, ponto_inferior_esquerdo):
        self.largura = largura
        self.altura = altura
        self.ponto_inferior_esquerdo = ponto_inferior_esquerdo

    def encontrar_centro(self):
        centro_x = self.ponto_inferior_esquerdo.x + self.largura / 2
        centro_y = self.ponto_inferior_esquerdo.y + self.altura / 2
        return Ponto(centro_x, centro_y)


# Função para imprimir um menu interativo
def exibir_menu():
    print("1. Imprimir ponto inferior esquerdo")
    print("2. Encontrar e imprimir centro do retângulo")
    print("3. Sair")


# Criar um objeto Retangulo
ponto_inferior_esquerdo = Ponto(0, 0)
retangulo = Retangulo(4, 3, ponto_inferior_esquerdo)

# Menu interativo
escolha = 0
while escolha != 3:
    exibir_menu()
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        ponto_inferior_esquerdo.imprimir()
    elif escolha == 2:
        centro = retangulo.encontrar_centro()
        centro.imprimir()
    elif escolha == 3:
        print("Programa encerrado.")
    else:
        print("Opção inválida. Tente novamente.")




#10
class BombaCombustivel:
    # R$ 5,63 gasolina_comum
    # R$ 5,82 gasolina_aditivada
    # R$ 3,64 alcool
    # R$ 6,12 disel

    global gasolina_comum
    global gasolina_aditivada
    global alcool
    global disel

    def __init__(self: object, tipoCombustivel: str, qtdCombustivel: float = 0.0):
        self.__tipoCombustivel = tipoCombustivel
        self.__qtdCombustivel = qtdCombustivel

    def abastecerPorValor(self: object, valor: int):
        if self.__tipoCombustivel in ['alcool', 'gasolina aditivada', 'etanol', 'disel', 'gasolina comum']:
            if self.__tipoCombustivel == 'alcool':
                alcool = 3.64
                self.__qtdCombustivel = valor / alcool
                print(f'Foram abastecidos [{self.__qtdCombustivel.__round__(1)}L] com o R${valor}')
            elif self.__tipoCombustivel == 'etanol':
                alcool = 3.64
                self.__qtdCombustivel = valor / alcool
                print(f'Foram abastecidos [{self.__qtdCombustivel.__round__(1)}L] com o R${valor}')
            elif self.__tipoCombustivel == 'disel':
                disel = 6.12
                self.__qtdCombustivel = valor / disel
                print(f'Foram abastecidos [{self.__qtdCombustivel.__round__(1)}L] com o R${valor}')
            elif self.__tipoCombustivel == 'gasolina comum':
                gasolina_comum = 5.63
                self.__qtdCombustivel = valor / gasolina_comum
                print(f'Foram abastecidos [{self.__qtdCombustivel.__round__(1)}L] com o R${valor}')
            elif self.__tipoCombustivel == 'gasolina aditivada':
                gasolina_aditivada = 5.82
                self.__qtdCombustivel = valor / gasolina_aditivada
                print(f'Foram abastecidos [{self.__qtdCombustivel.__round__(1)}L] com o R${valor}')
            else:
                print('Houve algum erro!')

        else:
            print('Combustivel indisponivel!')

    def abastecePorLitro(self: object, litros: int):
        if self.__tipoCombustivel in ['alcool', 'gasolina aditivada', 'etanol', 'disel', 'gasolina comum']:
            if self.__tipoCombustivel == 'alcool':
                alcool = 3.64
                self.__qtdCombustivel = litros
                print(f'Foram abastecidos [{self.__qtdCombustivel.__round__(1)}L] e ficou um total de [{self.__qtdCombustivel * alcool}]')
            elif self.__tipoCombustivel == 'etanol':
                alcool = 3.64
                self.__qtdCombustivel = litros
                print(f'Foram abastecidos [{self.__qtdCombustivel.__round__(1)}L] e ficou um total de [{self.__qtdCombustivel * alcool}]')
            elif self.__tipoCombustivel == 'disel':
                disel = 6.12
                self.__qtdCombustivel = litros
                print(f'Foram abastecidos [{self.__qtdCombustivel.__round__(1)}L] e ficou um total de [{self.__qtdCombustivel * disel}]')
            elif self.__tipoCombustivel == 'gasolina comum':
                gasolina_comum = 5.63
                self.__qtdCombustivel = litros
                print(f'Foram abastecidos [{self.__qtdCombustivel.__round__(1)}L] e ficou um total de [{self.__qtdCombustivel * gasolina_comum}]')
            elif self.__tipoCombustivel == 'gasolina aditivada':
                gasolina_aditivada = 5.82
                self.__qtdCombustivel = litros
                print(f'Foram abastecidos [{self.__qtdCombustivel.__round__(1)}L] e ficou um total de [{self.__qtdCombustivel * gasolina_aditivada}]')
            else:
                print('Houve algum erro!')

        else:
            print('Combustivel indisponivel!')




#11

class Carro:

    global distancia_km_lt

    def __init__(self: object, carro: str, capacidadeDoTanque: int, consumo: float, combustivelnoTanque: int = 0):
        self.__carro = carro
        self.__consumo = consumo
        self.__combustivelnoTanque = combustivelnoTanque
        self.__capacidadeDoTanque = capacidadeDoTanque

    def mostraNivelTanque(self: object):
        return f'O nivel de gasolina esta em [{self.__combustivelnoTanque}L]'

    def adicionarGasolina(self: object, gasolina: int):
        if gasolina <= self.__capacidadeDoTanque:
            self.__combustivelnoTanque += gasolina
        else:
            print(f'A capacidade do tanque insuficiente!')

    def andarCidade(self: object, distanciaEmKm: int):
        distancia_km_lt = distanciaEmKm / self.__consumo
        if distancia_km_lt <= self.__combustivelnoTanque:
            self.__combustivelnoTanque = self.__combustivelnoTanque - distancia_km_lt
            print(f'O carro percorreu [{distanciaEmKm}Km]')
        else:
            print(f'Nao eh possivel percorrer essa distancia com um tanque so com [{self.__capacidadeDoTanque}L]\n')
            print(f'Para percorrer a distancia sao necessarios [{(distanciaEmKm / self.__consumo) / self.__capacidadeDoTanque}] tanques cheios')

    def andarEstrada(self: object, distanciaEmKm: int):
        self.__consumo += (self.__consumo * 25) / 100
        distancia_km_lt = distanciaEmKm / self.__consumo
        if distancia_km_lt <= self.__combustivelnoTanque:
            self.__combustivelnoTanque = self.__combustivelnoTanque - distancia_km_lt
            print(f'O carro percorreu [{distanciaEmKm}Km]')
        else:
            print(f'Nao eh possivel percorrer essa distancia com um tanque so [{self.__capacidadeDoTanque}L]\n')
            print(f'Para percorrer a distancia sao necessarios [{(distanciaEmKm / self.__consumo) / self.__capacidadeDoTanque}] tanques cheios')




#12
class ContaInvestimento:

    contas = {}

    def __init__(self: object, numeroConta: int, nomeCorrentista: str, saldo: float = 1000.00):
        self.__numeroConta = numeroConta
        self.__nomeCorrentista = nomeCorrentista
        self.__saldo = saldo

    def alteraSaldo(self: object, valor):
        if valor > 0:
            self.__saldo = valor
        else:
            print('Informe um valor maior que zero!')

    def adicioneJuros(self: object):
        if self.__saldo > 0:
            self.__saldo += (self.__saldo * 10) / 100
        else:
            print('Saldo negativo!')

    def deposito(self: object, numeroContaDestino: int, valor: float):
        if valor > 0:
            numeroContaDestino = ContaInvestimento.contas.get(numeroContaDestino)
            if numeroContaDestino:
                numeroContaDestino.__saldo += valor
                self.__saldo -= valor
            else:
                print(f'O numero da conta [{numeroContaDestino}] nao existe.')
        else:
            print('O valor do deposito deve ser maior que zero.')

    def saque(self: object, valor: float):
        if valor > 0:
            if self.__saldo > valor:
                self.__saldo -= valor
            else:
                print('O correntista nao possui o saldo para efetuar o saque!')
        else:
            print('Informe um valor maior que zero.')

    def mostrarConta(self: object):
        return f'Numero da conta: {self.__numeroConta} | Nome do correntista: {self.__nomeCorrentista} | Saldo: {self.__saldo}'




#13
class Funcionario:

    def __init__(self: object, nome: str, salario: float):
        self.__nome = nome
        self.__salario = salario

    def mostraNome(self: object):
        return (f'O nome do funcionario: \n'
                f'{self.__nome}')

    def mostraSalario(self: object):
        return (f'O salario do funcionario: \n'
                f'{self.__nome} | R${self.__salario}')




#14
class Funcionario:

    def __init__(self: object, nome: str, salario: float):
        self.__nome = nome
        self.__salario = salario

    def mostraNome(self: object):
        return (f'O nome do funcionario: \n'
                f'{self.__nome}')

    def mostraSalario(self: object):
        return (f'O salario do funcionario: \n'
                f'{self.__nome} | R${self.__salario}')
    def aumentoSalario(self: object, valor: float):
        if valor > 0:
            self.__salario += (self.__salario * valor) / 100
        else:
            print('Informe um valor maior que zero!')




#15
class BichinhoVirtualMelhorado:


    def __init__(self: object, nome: str, satisfacao: int = 0, saude: int = 0, idade: int = 0, atencao: int = 0):
        self.__nome = nome
        self.__satisfacao = satisfacao
        self.__saude = saude
        self.__idade = idade
        self.__atencao = atencao

    def alterarNome(self: object, nome: str):
        self.__nome = nome

    def mostraNome(self):
        return self.__nome

    def alterarFome(self: object, satisfacao: int):
        self.__satisfacao = satisfacao

    def mostraFome(self):
        return self.__satisfacao

    def alterarSaude(self: object, saude: int):
        self.__saude = saude

    def mostraSaude(self):
        return self.__saude

    def alterarIdade(self: object, idade: int):
        self.__idade = idade

    def mostraIdade(self: object):
        return self.__idade

    def alteraSatisfacao(self: object, satisfacao: int):
        self.__satisfacao = satisfacao

    def mostraSatisfacao(self: object):
        return self.__satisfacao

    def mostraHumor(self):
        if self.__satisfacao + self.__atencao >= 180:
            print(f'O Tamagushi esta MUITO feliz {'\U0001F604'}')
            print(f'Ele esta com o humor de [{(self.__satisfacao + self.__atencao) / 2}]')
        elif self.__satisfacao + self.__atencao >= 150:
            print(f'O Tamagushi esta feliz {'\U0001F60A'}')
            print(f'Ele esta com o humor de [{(self.__satisfacao + self.__atencao) / 2}]')
        elif self.__satisfacao + self.__atencao >= 100:
            print(f'O Tamagushi nao esta nem triste e nem feliz {'\U0001F610'}')
            print(f'Ele esta com o humor de [{(self.__satisfacao + self.__atencao) / 2}]')
        elif self.__satisfacao + self.__atencao >= 50:
            print(f'O Tamagushi esta triste {'\U0001F641'}')
            print(f'Ele esta com o humor de [{(self.__satisfacao + self.__atencao) / 2}]')
        elif self.__satisfacao + self.__atencao >= 0:
            print(f'O Tamagushi esta MUITO triste {'\U0001F62D'}')
            print(f'Ele esta com o humor de [{(self.__satisfacao + self.__atencao) / 2}]')
        else:
            print('Valores citados incompativeis!!!')

    def mostraTudo(self: object):
        print(f'O nome do Tamagushi eh {self.__nome}')
        print(f'O/A {self.__nome} esta [{self.__satisfacao}%] satisfeito')
        print(f'O/A {self.__nome} esta [{self.__saude}%] saudavel')
        print(f'O/A {self.__nome} tem [{self.__idade}] anos')
        print(f'O/A {self.__nome} recebeu [{self.__atencao}%] de atencao')
"""

#16 #teste





















































