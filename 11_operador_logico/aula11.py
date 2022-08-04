"""
Operadores Lógicos
and, or, not
in e not in
"""
nome = 'Derick Castro'

#if 'r' in nome:
#   print("Existe a letra R no seu nome.")
#else:
#    print("Não existe")

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'derick'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário ou senha inválidos.')