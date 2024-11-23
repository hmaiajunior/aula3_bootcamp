# Exercício 01: Verificação de Qualidade de Dados

#Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

# quantidade = 120
# preco = 10

# if quantidade > 0 and preco > 0: 
#     print("Valores validos")
# else:
#     print("Valores invalidos")


# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))



# Exercício 06:  Contagem de Palavras em Textos

# Dado um texto, contar quantas vezes cada palavra única aparece nele


texto = "o rato roeu a roupa do rei de roma em roma"
palavras_sem_tratamento = texto
palavras_tratadas = palavras_sem_tratamento.replace(",","").split()

contagem_palavras = {}

for palavra in palavras_tratadas:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)