# Imagem do nodejs
FROM node:alpine

# Diretório onde vai estar a aplicação dentro do container
WORKDIR /usr/app

# Copiando o arquivo de dependências para dentro do container e instalando as dependências
COPY package.json ./
RUN npm install --silent

# Copiando o resto dos arquivos e rodando o build da aplicação
COPY . .
RUN npm run build

# Rodando a aplicação
CMD ["node", "client.js"]
