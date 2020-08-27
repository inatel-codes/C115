from socket import *
from termcolor import colored # Biblioteca para alterar cores nos prints

# Json formatado com as opções
options = {
  "message": "\nOla, seja bem vindo!\n\nDigite 1 para total de casos da COVID-19\nDigite 2 para ver informações sobre saúde",
  "options": {
    "1": {
      "message": "Digite 1 para casos no Mundo\nDigite 2 para casos no Brasil\nDigite 3 para casos em Minas Gerais",
      "options": {
        "1": "Atualmente o mundo se encontra com " + colored('24.011.502', 'red') + " casos",
        "2": "Atualmente o Brasil se encontra com " + colored('3.717.156', 'red') + " casos",
        "3": "Atualmente Minas Gerais se encontra com " + colored('201.973', 'red') + " casos",
      }
    },
    "2": {
      "message": "Digite 1 para medidas de prevenção\nDigite 2 para sintomas mais comuns\nDigite 3 para sintomas menos comuns",
      "options": {
        "1": "- Use máscara \n- Lave suas mãos \n- Mantenha uma distância segura",
        "2": "- Febre \n- Tosse seca \n- Cansaço",
        "3": "- Dores e desconfortos \n- Dor de garganta \n- Dor de cabeça \n- Perda de paladar ou olfato",
      }
    }
  }
}

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

  # Envia as primeiras opções e recebe a resposta do cliente
  connectionSocket.send(options["message"].encode())
  option1 = connectionSocket.recv(1024).decode()

  # Envia as segundas opções e recebe a resposta do cliente
  connectionSocket.send(options["options"][option1]["message"].encode())
  option2 = connectionSocket.recv(1024).decode()

  # Envia o resultado para o cliente
  connectionSocket.send(options["options"][option1]["options"][option2].encode())

  # Fecha a conexão
  connectionSocket.close()