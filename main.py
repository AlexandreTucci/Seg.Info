import json

with open ('base_de_autorização.json', "r") as arquivo:
    base = json.load(arquivo)
with open ('usuario.json', 'r') as arquivo:
    usuarios = json.load(arquivo)
 

base[0]['permissoes'][0]["escrita"] = True
base[0]['permissoes'][0]["excecucao"] = False


with open ('base_de_autorização.json', 'w') as arquivo:
    base_autorizacao = json.dump(base, arquivo , ensure_ascii=False)
    
def login(usuario, senha):
    for i in range(len(usuarios)):
        if usuarios[i]['usuario'] == usuario and usuarios[i]['senha'] == senha:
            print('Seja Bem Vindo ' + usuario)
        else:
            print('Login ou senha incorreto. Tente novamente mais tarde.')
            login(input('usuario:'), input('senha:'))
    return usuario

def cadastro(usuario, senha, usuarios):
    for i in range(len(usuarios)):
        if usuarios[i]['usuario'] == usuario:
            print('Usuário já existe. Tente novamente.')
            cadastro(input('Usuário: '), input('Senha: '))
        else:
            usuarios.append({'usuario': usuario, 'senha': senha})
            with open ('usuario.json', 'w') as arquivo:
                usuarios = json.dump(usuarios, arquivo , ensure_ascii=False)
    


def interface(usuarios):
    print('1. Login')
    print('2. Cadastro')
    print('3. Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        usuario = input('Usuário: ')
        senha = input('Senha: ')
        login(usuario, senha)
    elif opcao == '2':
        usuario = input('Usuário: ')
        senha = input('Senha: ')
        cadastro(usuario, senha, usuarios)
    elif opcao == '3':
        exit()
    else:
        print('Opção inválida. Tente novamente.')

interface(usuarios)