def adicionarProduto(listaProdutos):
    nome_produto = input("Digite o nome do produto: ")
    quantidade_produto = int(input("Digite a quantidade do produto: "))
    descricao_produto = input("Digite o descricao: ")

    while True:
        print("A. Quilograma")
        print("B. Grama")
        print("C. Litro")
        print("D. Militro")
        print("E. Unidade")
        print("F. Metro")
        print("G. Centímetro")

        unidade_medida_produto = input("Escolha a unidade de medida do produto: ")

        if unidade_medida_produto not in ("A", "B", "C", "D", "E", "F", "G"):
            print("Unidade de medida inválida! Digite novamente")
            continue
        else:
            novo_produto = {
                "id": len(listaProdutos) + 1,
                "nome": nome_produto,
                "quantidade": quantidade_produto,
                "descricao": descricao_produto,
                "unidade": unidade_medida_produto
            }
            print("Produto adicionado com sucesso!")
            return novo_produto

def removerProduto(listaProdutos):
    id_produto = int(input("Digite o id do produto: "))
    for produto in listaProdutos:
        if produto["id"] == id_produto:
            print("Produto removido com sucesso!")
            return produto
    print("Id não encontrado!")

def pesquisarProduto(listaProdutos):
    nome_produto = input("Digite o nome do produto: ")
    cont = 0

    for produto in listaProdutos:
        if produto["nome"] == nome_produto:
            print(f"{produto['nome']}")
            cont += 1

    print(f"Quantidade de produtos encontrados: {cont}")

def mostrarProdutos(listaProdutos):
    for produto in listaProdutos:
        print(f"ID: {produto['id']} | {produto['nome']} ({produto['quantidade']} {produto['unidade']})")

print("Olá, esta é uma lista de compras simples.")