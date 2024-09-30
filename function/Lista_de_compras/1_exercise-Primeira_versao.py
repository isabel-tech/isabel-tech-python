'''Primeira versão da lista de compras
Escreva um programa que permita que um usuário crie uma lista de compras. O usuário deve ser capaz de adicionar itens, remover itens e visualizar a lista.

Estruture seu programa da seguinte forma:

Crie uma lista vazia para armazenar os itens da lista de compras.
Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
Se o usuário escolher adicionar um item, solicite que ele digite o nome do item e adicione-o à lista.
Se o usuário escolher remover um item, solicite que ele digite o nome do item e remova-o da lista.
Se o usuário escolher ver a lista, mostre cada item da lista em sua própria linha.
Se o usuário escolher sair, encerre o loop usando break.
Exemplo de saída:

1 Adicionar item
2 Remover item
3 Ver lista
4 Sair
Escolha uma opção: 1
Digite um item: banana
'''
lista = []
opcoes = [1, 2, 3, 4]
while True:
	print('1- Adicionar Item')
	print('2- Remover Item')
	print('3- Ver Lista')
	print('4- Sair')
	escolher_opcao = int(input('Escolha uma opção: '))
	while escolher_opcao not in opcoes:
		print('Digite uma opção válida ')
		escolher_opcao = int(input('Escolha uma opção: '))
	if escolher_opcao == 1:
		digitar_item = input('Digite o item: ')
		lista.append(digitar_item)
	elif escolher_opcao == 2:
		digitar_item = input('Digite o item: ')
		if digitar_item in lista:
			lista.remove(digitar_item)
		else: 
			print('Item não encontrado na lista')
	elif escolher_opcao == 3:
		print(lista)
	else:
		print('Volte Sempre!')
		break
		