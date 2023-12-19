"""
# testando as alteracoes nos projetos
from main import Macaco

macaco = input('Informe o nome do macaco: ')
macaco = Macaco(macaco)
print('Caso queira que o macaco pare de comer digite "Sair"')

while True:
    comida = input('Informe o que o macaco vai comer: ')
    comida = comida.lower()
    if comida != 'sair':
        macaco.comer(comida)
    else:
        print('O macaco parou de comer!')
        break

print(macaco.verBucho())
macaco.digerir()
print(macaco.verBucho())



from main import BombaCombustivel

print('Combustiveis disponiveis na bomba: Etanol, Gasolina comum, Gasolina aditivada, Disel.')
combustivel = input('Informe qual combustivel ira abastecer: \n')
abastecimento = input('Informe a forma de abastecimento, por litro ou por valor: \n')
valor = int(input('Informe o valor em inteiro que vai pagar ou quantos litros ira abastecer: \n'))
combustivel = combustivel.lower()
abastecimento = abastecimento.lower()
carro = BombaCombustivel(combustivel)

if abastecimento == 'litro':
    carro.abastecePorLitro(valor)
elif abastecimento == 'valor':
    carro.abastecerPorValor(valor)
else:
    print('Forma indisponivel')




from main import Carro

carro = Carro('Gol', 55, 10.0, 10)

carro.andarCidade(10)
print(carro.mostraNivelTanque())
carro.andarCidade(10)
print(carro.mostraNivelTanque())
carro.andarEstrada(10)
print(carro.mostraNivelTanque())



from main import Funcionario
from time import sleep


def main():

    nome = str(input('Informe o nome do funcionario: \n'))
    salario = float(input('Informe o salario do funcionario: (ex: 1234.34)\n'))
    clt = Funcionario(nome, salario)

    menu = int(input(
        '1- Para mostrar o nome | 2- Para mostrar o salario | 3- Para acrescentar um aumento em % | 4- Para sair do programa: \n'))
    sleep(1)

    while True:
        if menu == 1:
            print(clt.mostraNome())
            sleep(1)
            menu = int(input('1- Para mostrar o nome | 2- Para mostrar o salario | 3- Para acrescentar um aumento em % | 4- Para sair do programa: \n'))
        elif menu == 2:
            print(clt.mostraSalario())
            sleep(1)
            menu = int(input('1- Para mostrar o nome | 2- Para mostrar o salario | 3- Para acrescentar um aumento em % | 4- Para sair do programa: \n'))

        elif menu == 3:
            aumento = int(input('Informe quantos % o salario sera aumentado: \n'))
            clt.aumentoSalario(aumento)
            sleep(1)
            menu = int(input('1- Para mostrar o nome | 2- Para mostrar o salario | 3- Para acrescentar um aumento em % | 4- Para sair do programa: \n'))
        elif menu == 4:
            print('Programa encerrado')
            break

        else:
            print('Selecione uma opcao valida')
            sleep(1)
            menu = int(input('1- Para mostrar o nome | 2- Para mostrar o salario | 3- Para acrescentar um aumento em % | 4- Para sair do programa: \n'))
"""
















