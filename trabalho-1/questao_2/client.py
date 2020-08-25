from socket import *
import pickle

serverName = 'localhost'
serverPort = 5000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

questions = pickle.loads(clientSocket.recv(1024))

answers = []

for question in questions:
  print("")
  print(question["message"])
  print(question["options"]["a"])
  print(question["options"]["b"])
  print(question["options"]["c"])
  print(question["options"]["d"])

  answer = input("Escolha uma opção: ")
  answers.append(answer)

clientSocket.sendall(pickle.dumps(answers))
response = clientSocket.recv(1024).decode()
print(response)

clientSocket.close()