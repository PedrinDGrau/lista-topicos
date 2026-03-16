DICIONARIO

aluno = {
    'nome': 'Pedro',
    'matricula': 123456,
    'turma': 'E',
    'notas': [7.5, 8, 5]
}

print (aluno)
print ("nome", aluno ['nome'])
print ("notas:", aluno ['notas'])
'''--------------------------'''
'''
contato = {
    'nome': 'Pedro',
    'telefone': 99996767,
    'email': 'PaulinDaOnça@gmail.com',
    'cidade': 'RioTiete'
}

print ("Itens do dicionario")
print (contato.keys())
'''
'''--------------------'''

contato = {
    'nome': 'Pedro',
    'telefone': 99996767,
    'email': 'PaulinDaOnça@gmail.com',
    'cidade': 'Rio Tiete',
}

contato['Instagram'] = 'Artur(irmao do mini pedro)'

del contato['telefone']

print(contato)
print(contato.get('Instagram'))

if 'email' in contato:
    print("xave achada")
