# integrantes: 
# Alexandre Andrioli Tucci
# João Victor Saboya Ribeiro de Carvalho

import json

with open ('base_de_autorizacao.json', "r") as arquivo:
    base = json.load(arquivo)
with open ('usuario.json', 'r') as arquivo:
    usuarios = json.load(arquivo)

def login(usuario, senha, usuarios, base):
    for i in range(len(usuarios)):
        if usuarios[i]['usuario'] == usuario and usuarios[i]['senha'] == senha:
            print('Seja Bem Vindo ' + usuario)
            InterfacePermissoes(usuario, base)
            return
    print('Login ou senha incorreto. Tente novamente mais tarde.')
    return

def cadastro(usuario, senha, usuarios, base):
    for i in range(len(usuarios)):
        if usuarios[i]['usuario'] == usuario:
            print('Usuário já existe. Tente novamente.')
            interface(usuarios, base)
            return
    usuarios.append({'usuario': usuario, 'senha': senha})
    with open ('usuario.json', 'w') as arquivo:
        writeUsuarios = json.dump(usuarios, arquivo , ensure_ascii=False)
    base.append(
            {'usuario': usuario, 
            'permissoes': {
                    "arquivo": "recurso.c",
                    "leitura": False,
                    "escrita": False,
                    "exclusao": False
                }
            }
        )
    with open ('base_de_autorizacao.json', 'w') as arquivo:
        base = json.dump(base, arquivo , ensure_ascii=False)
    with open ('base_de_autorizacao.json', 'r') as arquivo:
        base = json.load(arquivo)
    InterfacePermissoes(usuario, base)
    

def InterfacePermissoes(usuario, base):
    print(usuario)
    permissao = escolherPermissao()
    nomeArquivo = escolherArquivo()
    for i in range(len(base)):
        if base[i]['usuario'] == usuario:
            permissoes = base[i]['permissoes']
            if (permissao == 'ler' and permissoes['leitura']) or \
               (permissao == 'escrever' and permissoes['escrita']) or \
               (permissao == 'apagar' and permissoes['exclusao']):
                print(f'Acesso Permitido')
            else:
                print(f'Acesso Negado')

def escolherPermissao():
    print('1. Ler')
    print('2. Escrever')
    print('3. Apagar')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        permissao = 'ler'
    elif opcao == '2':
        permissao = 'escrever'
    elif opcao == '3':
        permissao = 'apagar'
    else:
        print('Opção inválida. Tente novamente.')
        return escolherPermissao()
    return permissao

def escolherArquivo():
    nomeArquivo = input('Escolha um arquivo: ')
    return nomeArquivo

def interface(usuarios, base):
    print('Bem-vindo ao sistema de autenticação!')
    print('1. Login')
    print('2. Cadastro')
    print('3. Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        usuario = input('Usuário: ')
        senha = input('Senha: ')
        login(usuario, senha, usuarios, base)
    elif opcao == '2':
        usuario = input('Usuário: ')
        senha = input('Senha: ')
        cadastro(usuario, senha, usuarios, base)
    elif opcao == '3':
        exit()
    else:
        print('Opção inválida. Tente novamente.')


interface(usuarios, base)