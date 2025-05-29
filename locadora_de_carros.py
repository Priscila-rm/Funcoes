def tracos():
    print('-' * 50)

tracos()
print(" seja bem vindo a locadora!!")
tracos()

nome = input ("Digite seu nome: ")
print(f'Olá, {nome}! Estamos felizes em tê-lo conosco.')
tracos()

print ("Selecione o carro que deseja alugar: ")

def mostra_opcoes():
    """Mostra as opções de carros disponiveis para aluguel."""
    print("1 - BMW")
    print("2 - MUSTANG")
    print("3 - HB20")
    print("4 - FUSCA")
    print("5 - CIVIC")
    print("0 - SAIR")

mostra_opcoes()


carro = int(input("Digite o carro que desejar alugar: "))

tracos()

match carro :
    case 1:
        print("BMW")
    case 2:
        print("MUSTANG")
    case 3:
        print("HB20")
    case 4: 
        print("FUSCA")
    case 5:
        print("CIVIC")
    case 0:
        print("Saindo do programa...")
        exit()
    case _:
        print("Codigo Invalido. Por favor, selecione um codigo do menu.")


