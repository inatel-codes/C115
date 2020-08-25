from socket import *
from termcolor import colored
import pickle

questions = [
  {
    "message": "1) Que protocolo permite a troca de datagramas IP, sem confirmações e sem garantia de entrega?",
    "options": {
        "a": "a) UDP",
        "b": "b) FTP",
        "c": "c) SMTP",
        "d": "d) TCP"
    },
    "answer": "a"
  },
  {
    "message": "2) Qual das seguintes alternativas é um protocolo da camada de transporte do modelo TCP/IP?",
    "options": {
        "a": "a) FTP",
        "b": "b) SMTP",
        "c": "c) TFTP",
        "d": "d) TCP"
    },
    "answer": "d"
  }
]

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)

serverSocket.settimeout(1000)

print("Server is ready")

while True:
  connectionSocket, addr = serverSocket.accept()
  connectionSocket.sendall(pickle.dumps(questions))
  answers = pickle.loads(connectionSocket.recv(1024))
  
  response = ""

  for index, question in enumerate(questions):
    response = response + "\nResposta da questão " + str(index+1) + ": " + question["answer"].upper() + "\n"

    if(answers[index] == questions[index]["answer"]):
      response = response + colored('Você acertou :)', 'green') + "\n"
    else:
      response = response + colored('Você errou :(', 'red') + "\n"

  connectionSocket.send(response.encode())

  connectionSocket.close()
