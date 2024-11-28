### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.



# quantidade = 120
# preco = 10

# if quantidade > 0 and preco > 0: 
#     print("Valores validos")
# else:
#     print("Valores invalidos")


# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))



### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.


# texto = "o rato roeu a roupa do rei de roma"
# palavras_tratadas = texto.replace(",","").split()

# contagem_palavras = {}

# for palavra in palavras_tratadas:
#     if palavra in contagem_palavras:
#         contagem_palavras[palavra] += 1
#     else:
#         contagem_palavras[palavra] = 1

# print(contagem_palavras)



### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.



### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.


vendas = [
    {"categoria": "eletronicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletronicos", "valor": 800},
    {"categoria": "eletronicos", "valor": 400},
    {"categoria": "livros", "valor": 250},
]

vendas_categoria = {}

for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in vendas_categoria:
        vendas_categoria[categoria] += valor
    else:
        vendas_categoria[categoria] = valor

    print(vendas_categoria)

