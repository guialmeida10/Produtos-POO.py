from Livro import Livro
from PecaCarro import PecaCarro
from Alimenticio import Alimenticio

def criar_livro():
    print("\nCadastro de Livro")
    codigo = int(input("Codigo: "))
    descricao = input("Descricao: ")
    preco = float(input("Preco: "))
    quantidade = int(input("Quantidade: "))
    autor = input("Autor: ")
    numero_paginas = int(input("Numero de Paginas: "))
    return Livro(codigo, descricao, preco, quantidade, autor, numero_paginas)

def criar_peca_carro():
    print("\nCadastro de Peça de Carro")
    codigo = int(input("Codigo: "))
    descricao = (input("Descricao: "))
    preco = float(input("Preco: "))
    quantidade = int(input("Quantidade: "))
    tipo_carro = input("Tipo do Carro: ")
    modelo = input("Modelo: ")
    return PecaCarro(codigo, descricao, preco, quantidade, tipo_carro, modelo)

def criar_alimento():
    print("\nCadastro de Produto Alimenticio")
    codigo = int(input("Codigo: "))
    descricao = (input("Descricao: "))
    preco = float(input("Preco: "))
    quantidade = int(input("Quantidade: "))
    validade = input("Data de Validade: ")
    return Alimenticio(codigo, descricao, preco, quantidade, validade)


def main():
    livros = []
    pecas = []
    alimentos = []

    while True:
        print("\nMENU")
        print("1 - Criar produto")
        print("2 - Mudar estoque")
        print("3 - Calcular valor total em estoque")
        print("4 - Imprimir todos os produtos de um tipo")
        print("5 - Imprimir todos os produtos cadastrados")
        print("0 - Sair")
        opcao = input("Escolha uma opcao: ")

        if opcao == '1':
            print("\nQual tipo de produto deseja criar?")
            print("1 - Livro")
            print("2 - Peça de carro")
            print("3 - Alimenticio")
            tipo = input("Escolha: ")

            if tipo == '1':
                livros.append(criar_livro())
                print("Livro adicionado com sucesso!")
            elif tipo == '2':
                pecas.append(criar_peca_carro())
                print("Peca adicionada com sucesso!")
            elif tipo == '3':
                alimentos.append(criar_alimento())
                print("Produto alimenticio adicionado!")
            else:
                print("Tipo invalido!")

        elif opcao == '2':
            print("\nEscolha o tipo de produto:")
            print("1 - Livro")
            print("2 - Peca de carro")
            print("3 - Alimenticio")
            tipo = input("Escolha: ")

            lista = None
            if tipo == '1':
                lista = livros
            elif tipo == '2':
                lista = pecas
            elif tipo == '3':
                lista = alimentos
            else:
                print("Tipo invalido!")
                continue

            if len(lista) == 0:
                print("Nenhum produto desse tipo cadastrado.")
                continue

            for p in lista:
                print(f"Codigo: {p.codigo} | Descricao: {p.descricao} | Qtd: {p.quantidade} | Preco: {p.preco}")

            codigo = int(input("Informe o codigo do produto: "))
            qtd = int(input("Quantidade a alterar (+ adiciona / - remove): "))

            encontrado = False
            for p in lista:
                if p.codigo == codigo:
                    p.mudaEstoque(qtd)
                    print("Estoque atualizado!")
                    encontrado = True
                    break

            if not encontrado:
                print("Produto nao encontrado.")

        elif opcao == '3':
            print("\nCalcular valor de qual tipo?")
            print("1 - Livro")
            print("2 - Peca de carro")
            print("3 - Alimenticio")
            tipo = input("Escolha: ")

            if tipo == '1': lista = livros
            elif tipo == '2': lista = pecas
            elif tipo == '3': lista = alimentos
            else:
                print("Tipo invalido!")
                continue

            if len(lista) == 0:
                print("Nenhum produto cadastrado.")
                continue

            for p in lista:
                print(f"Codigo: {p.codigo} | Descricao: {p.descricao} | Qtd: {p.quantidade}")

            codigo = int(input("Codigo do produto: "))

            encontrado = False
            for p in lista:
                if p.codigo == codigo:
                    total = p.preco * p.quantidade
                    print(f"Valor total em estoque: R$ {total:.2f}")
                    encontrado = True
                    break

            if not encontrado:
                print("Produto nao encontrado.")

        elif opcao == '4':
            print("\nImprimir produtos de qual tipo?")
            print("1 - Livro")
            print("2 - Peça de carro")
            print("3 - Alimenticio")
            tipo = input("Escolha: ")

            if tipo == '1': lista = livros
            elif tipo == '2': lista = pecas
            elif tipo == '3': lista = alimentos
            else:
                print("Tipo invalido!")
                continue

            if len(lista) == 0:
                print("Nenhum produto cadastrado.")
                continue

            for p in lista:
                p.imprimeProduto()
                print("------------------")

        elif opcao == '5':
            print("\nLIVROS:")
            if len(livros) == 0:
                print("Nenhum livro cadastrado.")
            for l in livros:
                l.imprimeProduto()

            print("\nPECAS DE CARRO:")
            if len(pecas) == 0:
                print("Nenhuma peca cadastrada.")
            for p in pecas:
                p.imprimeProduto()

            print("\nPRODUTOS ALIMENTICIOS:")
            if len(alimentos) == 0:
                print("Nenhum alimento cadastrado.")
            for a in alimentos:
                a.imprimeProduto()

        elif opcao == '0':
            print("Saindo...")
            break

        else:
            print("Opcao invalida!")

if __name__ == "__main__":
    main()
