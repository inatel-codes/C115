from socket import *
from termcolor import colored # Biblioteca para alterar cores nos prints
import pickle # Biblioteca para enviar formato json pelo socket 

# Json contendo as perguntas escolhidas
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

# Porta do servidor  
serverPort = 5000
# Criando um socket com uma determinada familia e tipo
serverSocket = socket(AF_INET, SOCK_STREAM)
# Associando o servidor a um determinado endereço e porta
serverSocket.bind(('', serverPort))
# Configura e inicia o ouvinte TCP
serverSocket.listen(1)
# Tempo máximo que o servidor irá esperar pela resposta do cliente
serverSocket.settimeout(1000)

print("Server is ready")

while True:
  # Aceita a conexão
  connectionSocket, addr = serverSocket.accept()
  # Enviando as perguntas para o cliente
  connectionSocket.sendall(pickle.dumps(questions))
  # Recebendo as respostas do cliente
  answers = pickle.loads(connectionSocket.recv(1024))
  
  # Variavel para guardar a resposta formatada
  response = ""

  # Percorrendo e formatando as respostas
  for index, question in enumerate(questions): 
    response = response + "\n\nResposta da questão " + str(index+1) + ": " + question["answer"].upper() + "\n"

    if(answers[index] == questions[index]["answer"]):
      response = response + colored('Você acertou :)', 'green')
    else:
      response = response + colored('Você errou :(', 'red') 

  # Enviando o resultado para o cliente
  connectionSocket.send(response.encode())

  # Fechando a conexão
  connectionSocket.close()
