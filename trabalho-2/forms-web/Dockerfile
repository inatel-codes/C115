FROM node:13-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH
COPY package.json /app/package.json
RUN yarn install

COPY . /app
RUN yarn run build

COPY build /app/build
COPY client.js /app

CMD ["node", "client.js"]
