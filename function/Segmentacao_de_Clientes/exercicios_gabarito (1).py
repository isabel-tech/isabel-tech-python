#!/usr/bin/env python
# coding: utf-8

# # Exercícios de fixação 

# A seguir, você encontrará alguns exercícios para fixar os conceitos aprendidos no curso até agora. Os exercícios estão divididos por exemplos práticos da vida real:
# 
# - lista de compras
# - previsão de vendas
# - relatório de vendas
# - segmentação de clientes
# - analisador de texto
# 
# Para cada assunto, você encontrará ao menos um exercício. Nos casos onde há mais de um exercício para o mesmo assunto, você será convidado a resolver o mesmo problema de formas diferentes. Isso é proposital, pois o objetivo é que você pratique o que aprendeu e, ao mesmo tempo, aprenda novas formas de resolver um mesmo problema. Por exemplo, usando diferentes estruturas de dados, ou diferentes formas de iterar sobre uma estrutura de dados, ou, ainda, utilizando funções.
# 
# Tente resolver os exercícios sozinho. Se tiver dificuldades, consulte o material do curso e, se ainda assim não conseguir resolver, consulte a solução.

# ## Lista de compras

# ### Primeira versão da lista de compras

# Escreva um programa que permita que um usuário crie uma lista de compras.
# O usuário deve ser capaz de adicionar itens, remover itens e visualizar a lista.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie uma lista vazia para armazenar os itens da lista de compras.
# 2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
# 3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
# 4. Se o usuário escolher adicionar um item, solicite que ele digite o nome do item e adicione-o à lista.
# 5. Se o usuário escolher remover um item, solicite que ele digite o nome do item e remova-o da lista.
# 6. Se o usuário escolher ver a lista, mostre cada item da lista em sua própria linha.
# 7. Se o usuário escolher sair, encerre o loop usando break.
# 
# Exemplo de saída:
# 
# ```
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: banana
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: maçã
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# ['banana', 'maçã']
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 2
# Digite um item: banana
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# ['maçã']
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 4
# ```

# In[ ]:


# solução

lista_compras = []

while True:
    print()                                 # linha em branco no início
    
    print("1 Adicionar item")
    print("2 Remover item")
    print("3 Ver lista")
    print("4 Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        item = input("Digite um item: ")
        lista_compras.append(item)
    elif escolha == '2':
        item = input("Digite um item: ")
        if item in lista_compras:
            lista_compras.remove(item)
    elif escolha == '3':
        print(lista_compras)
    elif escolha == '4':
        break


# ### Segunda versão da lista de compras
# 

# Mude o programa de lista de compras para usar um dicionário ao invés de uma lista.
# O programa deve ter as mesmas funcionalidades, mas agora deve ser possível
# adicionar mais de uma unidade de um item na lista de compras. Ou seja, o dicionário
# deve armazenar o nome do item e a quantidade desejada pelo usuário. Por exemplo,
# se o usuário digitar "banana" e "2", o dicionário deve armazenar "banana" como chave
# e 2 como valor. A estrutura do dicionário ficaria assim: `{"banana": 2}`.
# 
# O programa deve permitir que o usuário adicione, remova e visualize o dicionário de compras.
# 
# Além disso, o programa deve mostrar uma mensagem de erro se o usuário tentar
# usar uma opção inválida do menu. Por exemplo, se o usuário digitar 5, o programa
# deve mostrar a mensagem "Opção inválida. Por favor, escolha uma opção válida." e
# mostrar o menu novamente. Além disso, o programa deve ser *case insensitive*, ou seja,
# "Maçã" e "maçã" devem ser considerados o mesmo item.
# 
# Exemplo de saída:
# 
# ```
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: banana
# Digite a quantidade: 2
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: maçã
# Digite a quantidade: 3
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# {'banana': 2, 'maçã': 3}
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 2
# Digite um item: banana
# Digite a quantidade: 1
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# {'banana': 1, 'maçã': 3}
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 4
# ```
# 

# In[ ]:


# solução

# observe que agora é um dicionário, não uma lista mais. Não confunda o nome da variável
# com o tipo de dado que ela armazena. O nome da variável é lista_compras, mas ela
# armazena um dicionário, não uma lista. O nome da variável é apenas uma convenção
# para facilitar a leitura do código, já que é usual no cotidiano falarmos lista de compras.
# Você poderia ter escolhido outro nome para a variável, como dicionario_compras, por exemplo.
# Ou, simplesmente compras. 
# O importante é que o nome da variável seja significativo e facilite a leitura do código. 

lista_compras = {}

while True:
    print()
    
    print("1 Adicionar item")
    print("2 Remover item")
    print("3 Ver lista")
    print("4 Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        item = input("Digite um item: ").lower()
        quantidade = int(input("Digite a quantidade: "))
        if item in lista_compras:
            lista_compras[item] += quantidade
        else:
            lista_compras[item] = quantidade
    elif escolha == '2':
        item = input("Digite um item: ").lower()
        if item in lista_compras:
            quantidade = int(input("Digite a quantidade: "))
            if quantidade >= lista_compras[item]:
                del lista_compras[item]
            else:
                lista_compras[item] -= quantidade
        else:
            print("Item não está na lista de compras")
    elif escolha == '3':
        for item, quantidade in lista_compras.items():
            print(f"{item}: {quantidade}")
    elif escolha == '4':
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


# ### Terceira versão da lista de compras

# Mantenha o programa da lista de compras com dicionário, mas agora use funções para organizar o código. Crie funções para cada uma das opções do menu: `adicionar_item`, `remover_item` e `ver_lista`. Crie também uma função para mostrar o menu. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções.
# 

# In[ ]:


# solução
    
    
def adicionar_item(lista_compras):
    item = input("Digite um item: ").lower()
    quantidade = int(input("Digite a quantidade: "))
    if item in lista_compras:
        lista_compras[item] += quantidade
    else:
        lista_compras[item] = quantidade

        
def remover_item(lista_compras):
    item = input("Digite um item: ").lower()
    if item in lista_compras:
        quantidade = int(input("Digite a quantidade: "))
        if quantidade >= lista_compras[item]:
            del lista_compras[item]
        else:
            lista_compras[item] -= quantidade
    else:
        print("Item não está na lista de compras")
        

def ver_lista(lista_compras):
    for item, quantidade in lista_compras.items():
        print(f"{item}: {quantidade}")
        

def main():
    
    lista_compras = {}  
    
    while True:
        print()
        
        print("1 Adicionar item")
        print("2 Remover item")
        print("3 Ver lista")
        print("4 Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_item(lista_compras)
        elif escolha == '2':
            remover_item(lista_compras)
        elif escolha == '3':
            ver_lista(lista_compras)
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()


# ## Previsão de vendas

# ### Primeira versão da previsão de vendas

# Escreva um programa que preveja as vendas totais para cada produto em uma empresa.
# O usuário deve digitar o nome do produto, as vendas do mês atual e a taxa de crescimento,
# e o programa deve calcular as vendas previstas para o próximo mês.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie um dicionário vazio para armazenar as previsões de vendas.
# 2. Crie um loop infinito que solicite ao usuário o nome do produto, as vendas do mês atual e a taxa de crescimento.
# 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
# 4. Se o usuário digitar 'sair', encerre o loop usando break.
# 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular as vendas previstas e adicione-as ao dicionário.
# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar as previsões de vendas para cada produto.
# 
# Exemplo de saída:
# 
# ```
# Digite o nome do produto (ou 'sair' para sair): iphone
# Digite as vendas do mês atual: 10000
# Digite a taxa de crescimento (%): 10
# Digite o nome do produto (ou 'sair' para sair): capinha para iphone
# Digite as vendas do mês atual: 200
# Digite a taxa de crescimento (%): 20
# Digite o nome do produto (ou 'sair' para sair): sair
# iphone: Previsão de vendas do próximo mês = R$ 11000.00
# capinha para iphone: Previsão de vendas do próximo mês = R$ 240.00
# ```
# 

# In[ ]:


# solução

previsao = {}
while True:
    nome = input("Digite o nome do produto (ou 'sair' para sair): ")
    if nome.lower() == 'sair':
        break
    vendas_atual = float(input("Digite as vendas do mês atual: "))
    taxa_crescimento = float(input("Digite a taxa de crescimento (%): "))
    vendas_proximo_mes = vendas_atual * (1 + taxa_crescimento / 100)
    previsao[nome] = vendas_proximo_mes

for nome, vendas_proximo_mes in previsao.items():
    print(f"{nome}: Previsão de vendas do próximo mês = R$ {vendas_proximo_mes:.2f}")


# ### Segunda versão da previsão de vendas
# 

# Mantenha a mesma funcionalidade do programa anterior, mas agora valide a entrada do usuário.
# Se o usuário digitar um valor inválido para vendas ou taxa de crescimento, mostre a mensagem
# "Entrada inválida. Por favor, digite um número para vendas e taxa de crescimento." e peça
# para o usuário digitar novamente. Tal validação deve ser feita usando try/except.
# 

# In[ ]:


# solução

previsao = {}
while True:
    nome = input("Digite o nome do produto (ou 'sair' para sair): ")
    if nome.lower() == 'sair':
        break
    try:
        vendas_atual = float(input("Digite as vendas do mês atual: "))
        taxa_crescimento = float(input("Digite a taxa de crescimento (%): "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para vendas e taxa de crescimento.")
        continue
    vendas_proximo_mes = vendas_atual * (1 + taxa_crescimento / 100)
    previsao[nome] = vendas_proximo_mes

for nome, vendas_proximo_mes in previsao.items():
    print(f"{nome}: Previsão de vendas do próximo mês = R$ {vendas_proximo_mes:.2f}")


# ## Relatório de vendas

# ### Primeira versão do relatório de vendas

# Escreva um programa que calcula o total e a média de vendas para cada vendedor em uma empresa.
# O usuário deve digitar o nome do vendedor e suas vendas, e o programa deve manter o controle
# do total e da média de vendas para cada vendedor.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie um dicionário vazio para armazenar os dados de vendas.
# 2. Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
# 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
# 4. Se o usuário digitar 'sair', encerre o loop usando break.
# 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.
# 
# Exemplo de saída:
#     
# ```
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 100
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 200
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 300
# Digite o nome do vendedor (ou 'sair' para sair): sair
# João: Total de vendas = R$ 400.0, Média de vendas = R$ 200.0
# Maria: Total de vendas = R$ 200.0, Média de vendas = R$ 200.0
# ```
# 
# Dica: use o método sum() para calcular o total de vendas e o método len() para calcular o número de vendas.
# 

# In[ ]:


# solução

dados_vendas = {}
while True:
    nome = input("Digite o nome do vendedor (ou 'sair' para sair): ")
    if nome.lower() == 'sair':
        break
    vendas = float(input("Digite as vendas: "))
    if nome not in dados_vendas:
        dados_vendas[nome] = [vendas]
    else:
        dados_vendas[nome].append(vendas)

for nome, vendas in dados_vendas.items():
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    print(f"{nome}: Total de vendas = R$ {total_vendas:.2f}, Média de vendas = R$ {media_vendas:.2f}")


# ### Segunda versão do relatório de vendas
# 

# Mantenha a mesma funcionalidade do programa anterior, mas agora valide a entrada do usuário.
# Se o usuário digitar um valor inválido para vendas, mostre a mensagem
# "Entrada inválida. Por favor, digite um número para vendas." e peça para o usuário digitar
# novamente. Tal validação deve ser feita usando try/except.
# 
# Além disso, ao invés de armazenar cada venda em uma lista para cada vendedor, armazene
# o total de vendas e a quantidade de vendas em um dicionário. Por exemplo, se o usuário
# digitar "João" e "1000" para vendas, o dicionário deve ficar assim:
# 
# ```python
# {'João': {'total_vendas': 1000, 'quantidade_vendas': 1}}
# ```
# 
# Se, após, o usuário digitar "João" e "2000" para vendas, o dicionário deve ficar assim:
# 
# ```python
# {'João': {'total_vendas': 3000, 'quantidade_vendas': 2}}
# ```
# 
# Perceba como o total de vendas de João aumentou em 2000, assim como a quantidade aumentou em uma unidade.
# 
# Ao final, mostre o total de vendas e a média de vendas de cada vendedor.
# 
# Exemplo de saída:
# 
# ```
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 1000
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 2000
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 2000
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 3000
# Digite o nome do vendedor (ou 'sair' para sair): sair
# João: Total de vendas = R$ 3000.00, Média de vendas = R$ 1500.00
# Maria: Total de vendas = R$ 5000.00, Média de vendas = R$ 2500.00
# ```
# 

# In[ ]:


# solução

dados_vendas = {}
while True:
    nome = input("Digite o nome do vendedor (ou 'sair' para sair): ")
    if nome.lower() == 'sair':
        break
    try:
        vendas = float(input("Digite as vendas: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para vendas.")
        continue
    if nome not in dados_vendas:
        dados_vendas[nome] = {'total_vendas': vendas, 'quantidade_vendas': 1}
    else:
        dados_vendas[nome]['total_vendas'] += vendas
        dados_vendas[nome]['quantidade_vendas'] += 1

for nome, dados in dados_vendas.items():
    total_vendas = dados['total_vendas']
    media_vendas = total_vendas / dados['quantidade_vendas']
    print(f"{nome}: Total de vendas = R$ {total_vendas:.2f}, Média de vendas = R$ {media_vendas:.2f}")


# ### Terceira versão do relatório de vendas

#  Mantenha a funcionalidade do programa, mas agora use funções para organizar o código. Crie funções para cada uma das operações: `solicitar_nome_vendedor`, `solicitar_vendas` e `atualizar_dados` e `print_dados`. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções.

# In[ ]:


# solução


def solicitar_nome_vendedor():
    return input("Digite o nome do vendedor (ou 'sair' para sair): ").lower()


def solicitar_vendas():
    try:
        return float(input("Digite as vendas: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para vendas.")
        return None

    
def atualizar_dados(dados_vendas, nome, vendas):
    if nome not in dados_vendas:
        dados_vendas[nome] = {'total_vendas': vendas, 'quantidade_vendas': 1}
    else:
        dados_vendas[nome]['total_vendas'] += vendas
        dados_vendas[nome]['quantidade_vendas'] += 1
        

def print_dados(dados_vendas):
    for nome, dados in dados_vendas.items():
        total_vendas = dados['total_vendas']
        media_vendas = total_vendas / dados['quantidade_vendas']
        print(f"{nome}: Total de vendas = R$ {total_vendas:.2f}, Média de vendas = R$ {media_vendas:.2f}")
        

def main():
    dados_vendas = {}
    while True:
        nome = solicitar_nome_vendedor()
        if nome == 'sair':
            break
        vendas = solicitar_vendas()
        if vendas is None:
            continue
        atualizar_dados(dados_vendas, nome, vendas)
    print_dados(dados_vendas)

if __name__ == "__main__":
    main()


# ## Segmentação de clientes

# ### Primeira versão da segmentação de clientes

# Escreva um programa que segmenta clientes com base em suas compras totais.
# O usuário deve digitar o nome do cliente e suas compras totais, e o programa
# deve atribuir cada cliente a um segmento: 'Bronze' para compras de até R\\$ 1000,
# 'Prata' para compras de até R\\$ 5000 e 'Ouro' para compras acima de R\\$ 5000.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie um dicionário vazio para armazenar os clientes e seus segmentos.
# 2. Crie um loop infinito que solicite ao usuário o nome do cliente e suas compras totais.
# 3. Dentro do loop, use uma declaração if para atribuir o segmento apropriado ao cliente.
# 4. Se o usuário digitar 'sair' para o nome do cliente, encerre o loop usando break.
# 5. Fora do loop, use um loop for para imprimir o nome e o segmento de cada cliente.
# 
# Exemplo de saída:
#     
# ```
# Digite o nome do cliente (ou 'sair' para sair): João
# Digite o total de compras: 100
# Digite o nome do cliente (ou 'sair' para sair): Maria
# Digite o total de compras: 2000
# Digite o nome do cliente (ou 'sair' para sair): José
# Digite o total de compras: 6000
# Digite o nome do cliente (ou 'sair' para sair): sair
# João: Segmento do Cliente = Bronze
# Maria: Segmento do Cliente = Prata
# José: Segmento do Cliente = Ouro
# ```
# 

# In[ ]:


# solução

clientes = {}
while True:
    nome = input("Digite o nome do cliente (ou 'sair' para sair): ")
    if nome.lower() == 'sair':
        break
    compras = float(input("Digite o total de compras: "))
    if compras <= 1000:
        segmento = 'Bronze'
    elif compras <= 5000:
        segmento = 'Prata'
    else:
        segmento = 'Ouro'
    clientes[nome] = segmento

for nome, segmento in clientes.items():
    print(f"{nome}: Segmento do Cliente = {segmento}")


# ### Segunda versão da segmentação de clientes
# 

# 
# Mantenha a mesma funcionalidade do programa anterior, mas agora valide a entrada do usuário.
# Se o usuário digitar um valor inválido para compras, mostre a mensagem
# "Entrada inválida. Por favor, digite um número para compras." e peça para o usuário digitar
# novamente. Tal validação deve ser feita usando try/except.
# 
# Além disso, ao invés de deixar os limites de compras fixos no programa, armazene-os em uma
# lista de tuplas. Por exemplo:
# 
# ```python
# segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]
# ``` 
# 
# Assim, outros segmentos podem ser adicionados facilmente. O primeiro elemento da tupla é o
# limite de compras e o segundo é o nome do segmento. O último elemento da lista é uma tupla
# com limite `float('inf')`, que representa o segmento Ouro. Isso significa que, se o valor de
# compras for maior que todos os limites, o segmento será Ouro.
# 
# Depois, percorra essa lista e, para cada tupla, verifique se o valor de compras é menor ou igual
# ao limite. Se for, armazene o segmento em um dicionário. Por exemplo, se o usuário digitar
# "João" e "500" para compras, o dicionário deve ficar assim:
# `{'João': 'Bronze'}`
# 

# In[ ]:


# solução

segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]
clientes = {}
while True:
    nome = input("Digite o nome do cliente (ou 'sair' para sair): ")
    if nome.lower() == 'sair':
        break
    try:
        compras = float(input("Digite o total de compras: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para compras.")
        continue
    for limite, segmento in segmentos:
        if compras <= limite:
            clientes[nome] = segmento
            break

for nome, segmento in clientes.items():
    print(f"{nome}: Segmento do Cliente = {segmento}")


# ### Terceira versão da segmentação de clientes

# Mantenha a funcionalidade do programa, mas agora use funções para organizar o código. Crie funções para cada uma das operações: `solicitar_nome_cliente`, `solicitar_total_compras` e `atribuir_segmento` e `print_segmento_por_cliente`. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções. Além disso, normalize que todos os nomes sejam armazenados em letras minúsculas.

# In[ ]:


# solução


def solicitar_nome_cliente():
    return input("Digite o nome do cliente (ou 'sair' para sair): ").lower()


def solicitar_total_compras():
    try:
        return float(input("Digite o total de compras: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para compras.")
        return None
    

def atribuir_segmento(compras, segmentos):
    for limite, segmento in segmentos:
        if compras <= limite:
            return segmento
        

def print_segmento_por_cliente(clientes):
    for nome, segmento in clientes.items():
        print(f"{nome}: Segmento do Cliente = {segmento}")
        

def main():
    segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]
    clientes = {}
    while True:
        nome = solicitar_nome_cliente()
        if nome == 'sair':
            break
        compras = solicitar_total_compras()
        if compras is None:
            continue
        clientes[nome] = atribuir_segmento(compras, segmentos)
    print_segmento_por_cliente(clientes)

    
if __name__ == "__main__":
    main()


# ## Analisador de texto

# Crie um programa que analise um texto fornecido pelo usuário.
# O programa deve contar o número de palavras (independentemente se há repetição ou não),
# a quantidade de cada palavra e a
# quantidade de cada letra. Ignore maiúsculas e minúsculas ao contar letras.
# Não se preocupe com pontuação e espaços ao contar palavras.
# 
# O programa deve conter uma função chamada `analisar_texto` que recebe o texto
# como parâmetro e retorna a contagem de palavras, a frequência de palavras e a
# frequência de letras.
# 
# Para o texto "Olá mundo! Este é um teste. Olá novamente." o programa deve
# imprimir:
#     
# ```
# Contagem de palavras: 8
# Frequência de palavras: {'Olá': 2, 'mundo!': 1, 'Este': 1, 'é': 1, 'um': 1, 'teste.': 1, 'novamente.': 1}
# Frequência de letras: {'o': 4, 'l': 2, 'á': 2, 'm': 3, 'u': 2, 'n': 3, 'd': 1, '!': 1, 'e': 6, 's': 2, 't': 4, 'é': 1, '.': 2, 'v': 1, 'a': 1}
# ```
# 
# **Observação**: Mais adiante no curso, aprenderemos a lidar com a pontuação.

# In[ ]:


# solução


def analisar_texto(texto):
    
    palavras = texto.split()  # separa com base em espaços
    contagem_palavras = len(palavras)
    frequencia_palavras = {}
    frequencia_letras = {}
    
    for palavra in palavras:
        # abaixo, o get verificará se existe a palavra no dicionário. Não havendo, atribui o valor 0 e soma 1
        frequencia_palavras[palavra] = frequencia_palavras.get(palavra, 0) + 1
        for letra in palavra.lower():
            # abaixo, o get verificará se existe a letra no dicionário. Não havendo, atribui o valor 0 e soma 1
            frequencia_letras[letra] = frequencia_letras.get(letra, 0) + 1
            
    return contagem_palavras, frequencia_palavras, frequencia_letras


texto = "Olá mundo! Este é um teste. Olá novamente."
contagem_palavras, frequencia_palavras, frequencia_letras = analisar_texto(texto)
print(f"Contagem de palavras: {contagem_palavras}")
print(f"Frequência de palavras: {frequencia_palavras}")
print(f"Frequência de letras: {frequencia_letras}")

