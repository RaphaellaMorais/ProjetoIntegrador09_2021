from socket import *
#configura conexão
HOST = '10.0.0.13'
PORTA = 100
#estabelece a conexão
conexao = socket(AF_INET, SOCK_STREAM)
conexao.connect((HOST, PORTA))

while True:
    #envia dados
    user = input('Login: ')
    password = input('Senha: ')
    #usa a função send para enviar os dados codificado
    conexao.send(user.encode())
    conexao.send(password.encode())
    #recebe dados e decodifica para string novamente
    resposta = conexao.recv(1024).decode()

    if resposta == 'Sucesso':
        print('Login realizado com sucesso!')
        break
    else:
        print('Login ou Senha inválida! Digite novamente:')

conexao.close()
