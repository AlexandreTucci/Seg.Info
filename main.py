import json

with open ('base_de_autorizacao.json', "r") as arquivo:
    base = json.load(arquivo)
with open ('usuario.json', 'r') as arquivo:
    usuarios = json.load(arquivo)
    
def login(usuario, senha, usuarios, base):
    for i in range(len(usuarios)):
        if usuarios[i]['usuario'] == usuario and usuarios[i]['senha'] == senha:
            print('Seja Bem Vindo ' + usuario)
            return
    print('Login ou senha incorreto. Tente novamente mais tarde.')
    interface(usuarios, base)        # login(input('usuario:'), input('senha:'))
    return usuario

def cadastro(usuario, senha, usuarios, base):
    for i in range(len(usuarios)):
        if usuarios[i]['usuario'] == usuario:
            print('Usuário já existe. Tente novamente.')
            interface(usuarios, base)
            return
            # cadastro(input('Usuário: '), input('Senha: '))
    usuarios.append({'usuario': usuario, 'senha': senha})
    with open ('usuario.json', 'w') as arquivo:
        usuarios = json.dump(usuarios, arquivo , ensure_ascii=False)
    base.append(
            {'usuario': usuario, 
            'permissoes': {
                    "arquivo": "recurso.c",
                    "leitura": False,
                    "escrita": False,
                    "execucao": False
                }
            }
        )
    with open ('base_de_autorizacao.json', 'w') as arquivo:
        base = json.dump(base, arquivo , ensure_ascii=False)
    InterfacePermissoes(usuario, base)
    

def InterfacePermissoes(usuario, base):
    permissao = escolherPermissao()
    nomeArquivo = escolherArquivo()
    for i in range(len(base)):
        if base[i]['usuario'] == usuario:
            if (permissao == 'ler' and base[i]['permissoes']['leitura'] == True) or (permissao == 'ler' and base[i]['permissoes']['escrita'] == True) or (permissao == 'ler' and base[i]['permissoes']['execucao'] == True):
                print('O usuario ' + usuario + ' tem permissão para ' + permissao + ' o arquivo ' + nomeArquivo)
            else:
                print('O usuario ' + usuario + 'NÃO tem permissão para ' + permissao + ' o arquivo ' + nomeArquivo)


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
        InterfacePermissoes()
    return permissao

def escolherArquivo():
    nomeArquivo = input('Escolha um arquivo: ')
    return nomeArquivo

def interface(usuarios, base):
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