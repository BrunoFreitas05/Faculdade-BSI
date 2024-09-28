const { createServer } = require("node:http");

const protocol = "http"
const hostName = "127.0.0.1";
const port = "3000";

const server = createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");
  res.end("Dev.Beck-end");
});

server.listen(port, hostName, () => { 
    console.log(`Servidor Rodando em ${protocol}://${hostName}:${port}`);
  });