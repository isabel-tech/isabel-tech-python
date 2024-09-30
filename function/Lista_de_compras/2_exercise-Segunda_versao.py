# Segunda versão da lista de compras

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
dicionario = {}
opcoes = ['1', '2', '3', '4']
while True:
	print('1- Adicionar Item')
	print('2- Remover Item')
	print('3- Ver Lista')
	print('4- Sair')
	escolher_opcao = input('Escolha uma opção: ')
	while escolher_opcao not in opcoes:
		print('Opção inválida. Por favor, escolha uma opção válida.')
		escolher_opcao = str(input('Escolha uma opção: '))
	if escolher_opcao == '1':
		digitar_item = input('Digite o item: ')
		digitar_item = digitar_item.lower()
		digitar_item = digitar_item.strip()
		qtde = int(input('Digite a quantidade: ' ))
		while (qtde <= 0):
			print('Digite uma quantidade válida.')
			qtde = int(input('Digite a quantidade: ' ))
		dicionario[digitar_item] = qtde
	elif escolher_opcao == '2':
		digitar_item = input('Digite o item: ')
		digitar_item = digitar_item.lower()
		digitar_item = digitar_item.strip()
		if digitar_item in dicionario:
			qtde_a_ser_removida = int(input('Digite a quantidade:'))
			if qtde_a_ser_removida < dicionario[digitar_item]:
				dicionario[digitar_item] -= qtde_a_ser_removida
			elif qtde_a_ser_removida == dicionario[digitar_item]:
				dicionario.pop(digitar_item)
			else:
				while qtde_a_ser_removida > dicionario[digitar_item]:
					qtde_a_ser_removida = int(input('Você digitou uma quantidade maior do que a quantidade existente. Digite um valor válido: '))
					if qtde_a_ser_removida < dicionario[digitar_item]:
						dicionario[digitar_item] -= qtde_a_ser_removida
					elif qtde_a_ser_removida == dicionario[digitar_item]:
						dicionario.pop(digitar_item)	
		else: 
			print('Item não encontrado na lista')
	elif escolher_opcao == '3':
		print(dicionario)
	else:
		print('Volte Sempre!')
		break
		
