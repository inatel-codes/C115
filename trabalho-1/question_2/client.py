from socket import *
import pickle # Biblioteca para enviar formato json pelo socket 

# Endereço do servidor
serverName = 'localhost'
# Porta do servidor
serverPort = 5000

# Criando um socket com uma determinada familia e tipo
clientSocket = socket(AF_INET, SOCK_STREAM)
# Estabelendo a conexão cliente-servidor
clientSocket.connect((serverName, serverPort))

# Recebendo as perguntas do servidor
questions = pickle.loads(clientSocket.recv(1024))

# Variavel para guardar as respostas do cliente
answers = []

# Percorrendo todas as perguntas e pegando a resposta do cliente
for question in questions:
  print("")
  print(question["message"])
  print(question["options"]["a"])
  print(question["options"]["b"])
  print(question["options"]["c"])
  print(question["options"]["d"])

  answer = input("Escolha uma opção: ")
  answers.append(answer)

# Enviando as respostas ao servidor
clientSocket.sendall(pickle.dumps(answers))
# Recebendo o resultado do servidor e mostrando para o cliente
response = clientSocket.recv(1024).decode()
print(response)

# Fechando a conexão
clientSocket.close()