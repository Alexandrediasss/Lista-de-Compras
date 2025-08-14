from funcoes_CRUD import mostrarProdutos
from funcoes_CRUD import pesquisarProduto
from funcoes_CRUD import removerProduto
from funcoes_CRUD import adicionarProduto

listaProdutos = []

while True:
    mostrarProdutos(listaProdutos)
    print("=== Lista de compras ===")
    print("A. Adicionar produto")
    print("B. Remover produto")
    print("C. Pesquisar Produto")
    print("D. Sair do programa")

    operador = input("Escolha uma das opções: ")

    if operador == "d" or operador == "D":
        print("Obrigado por usar o nosso programa!")
        break
    elif operador == "a" or operador == "A":
        listaProdutos.append(adicionarProduto(listaProdutos))
    elif operador == "b" or operador == "B":
        listaProdutos.remove(removerProduto(listaProdutos))
    elif operador == "c" or operador == "C":
        pesquisarProduto(listaProdutos)
    else:
        print("Operação inválida! Tente novamente.")