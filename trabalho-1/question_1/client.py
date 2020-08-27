from socket import *

# Endereço do servidor
serverName = 'localhost'
# Porta do servidor
serverPort = 5000

# Criando um socket com uma determinada familia e tipo
clientSocket = socket(AF_INET, SOCK_STREAM)
# Estabelendo a conexão cliente-servidor
clientSocket.connect((serverName, serverPort))

# Recebendo a mensagem do servidor com as opções e enviando a opção do cliente
message = clientSocket.recv(1024).decode()
print(message)
option = input("Opção: ")
print("")
clientSocket.send(option.encode())

# Recebendo a mensagem do servidor com as opções e enviando a opção do cliente
message = clientSocket.recv(1024).decode()
print(message)
option = input("Opção: ")
print("")
clientSocket.send(option.encode())

# Recebendo o resultado escolhido pelo cliente
message = clientSocket.recv(1024).decode()
print(message)

# Fechando a conexão
clientSocket.close()