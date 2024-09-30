# ### Terceira versão da lista de compras

# Mantenha o programa da lista de compras com dicionário, mas agora use funções para organizar o código. Crie funções para cada uma das opções do menu: `adicionar_item`, `remover_item` e `ver_lista`. Crie também uma função para mostrar o menu. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções.


dicionario = {}
opcoes = ['1', '2', '3', '4']

def mostrar_menu():
	print('1- Adicionar Item')
	print('2- Remover Item')
	print('3- Ver Lista')
	print('4- Sair')
	escolher_opcao = input('Escolha uma opção: ')
	while escolher_opcao not in opcoes:
		print('Opção inválida. Por favor, escolha uma opção válida.')
		escolher_opcao = str(input('Escolha uma opção: '))
	return escolher_opcao

def adicionar_item():
	digitar_item = input('Digite o item: ')
	digitar_item = digitar_item.lower()
	digitar_item = digitar_item.strip()
	qtde = int(input('Digite a quantidade: ' ))
	while (qtde <= 0):
		print('Digite uma quantidade válida.')
		qtde = int(input('Digite a quantidade: ' ))
	dicionario[digitar_item] = qtde
	return digitar_item, dicionario[digitar_item]

def remover_item():
	digitar_item = input('Digite o item: ')
	digitar_item = digitar_item.lower()
	digitar_item = digitar_item.strip()
	qtde_a_ser_removida = 0
	if digitar_item in dicionario:
		qtde_a_ser_removida = int(input('Digite a quantidade:'))
		while qtde_a_ser_removida > dicionario[digitar_item]:
			qtde_a_ser_removida = int(input('Você digitou uma quantidade maior do que a quantidade existente. Digite um valor válido: '))
		if qtde_a_ser_removida < dicionario[digitar_item]:
			dicionario[digitar_item] -= qtde_a_ser_removida
		elif qtde_a_ser_removida == dicionario[digitar_item]:
			dicionario.pop(digitar_item)	
	else: 
		print('Item não encontrado na lista')
	return digitar_item, qtde_a_ser_removida
		
def ver_lista():
	print(dicionario)
	return dicionario

while True:
	escolher_opcao = mostrar_menu()
	if escolher_opcao == '1':
		adicionar_item()
	elif escolher_opcao == '2':
		remover_item()
	elif escolher_opcao == '3':
		ver_lista()
	else:
		print('Volte sempre!')
		break