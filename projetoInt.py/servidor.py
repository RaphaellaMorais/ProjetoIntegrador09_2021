from socket import *
#configura conexão
HOST = '10.0.0.13'
PORTA = 100
#estabelece conexão
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((HOST, PORTA))
sockobj.listen(1)

while True:
    #aceita conexão do cliente
    conexao, endereco = sockobj.accept()
    print('Conectado', endereco)
    while True:
    #recebe informação e decodifica para string
        user = conexao.recv(1024)
        password = conexao.recv(1024)
        user = user.decode()
        password = password.decode()
        print('User: ', user)
        print('Password: ', password)
        user_no_servidor = 'raphaella'
        password_no_servidor = '123456'

        if user_no_servidor == user and password_no_servidor == password:
            resposta = 'Sucesso'
            conexao.send(resposta.encode())
            break
        else:
            resposta = 'Falha'
            conexao.send(resposta.encode())

    print('Desconectado', endereco)
    conexao.close()
