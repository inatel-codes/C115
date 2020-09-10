const express = require('express')

var http = require('http');

const appHttp = express()

const baseDir = `${__dirname}/build/`

// HTTP CONFIGURATION
appHttp.use(express.static(`${baseDir}`))
appHttp.get('*', (req, res) => res.sendFile('index.html', { root: baseDir }))

const portHttp = 3000

var httpServer = http.createServer(appHttp);
httpServer.listen(portHttp, () => console.log(`Servidor subiu com sucesso em http://localhost:${portHttp}`));