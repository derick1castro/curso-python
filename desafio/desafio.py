"""
* Criar variáveis para nome(str), idade(int),
* Altura(float) e peso(float) de uma pessoa
* Criar variável com o ano atual(int)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usndo F-Strings (com as chaves)
"""

nome = 'Derick Castro Domingos'
idade = 26
altura = 1.87
peso = 96
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f"{nome} tem {idade} anos, {altura} de altura e pesa {peso}.")
print(f"O IMC de {nome} é {imc:.2f}.")
print(f"{nome} nasceu em {nascimento}.")