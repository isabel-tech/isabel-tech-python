# ## Analisador de texto

# Crie um programa que analise um texto fornecido pelo usuário.
# O programa deve contar o número de palavras (independentemente se há repetição ou não),
# A quantidade de cada palavra e a quantidade de cada letra. Ignore maiúsculas e minúsculas ao contar letras.
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


def analisar_texto(texto):
	frequencia_palavras = {}
	frequencia_letras = {}

	palavras = texto.split()

	contagem_palavras = len(palavras)
	

	for palavra in palavras:
		palavra = palavra.strip('.,!?').lower()
		if palavra in frequencia_palavras:
			frequencia_palavras[palavra] += 1
		else: 
			frequencia_palavras[palavra] = 1
	
		for letra in palavra:
			if letra in frequencia_letras:
				frequencia_letras[letra] += 1
			else:
				frequencia_letras[letra] = 1
	return contagem_palavras, frequencia_palavras, frequencia_letras

texto = input('Digite o texto: ')
contagem_palavras, frequencia_palavras, frequencia_letras = analisar_texto(texto)
print(f"Contagem de palavras: {contagem_palavras}")
print(f"Frequência de palavras: {frequencia_palavras}")
print(f"Frequência de letras: {frequencia_letras}")


