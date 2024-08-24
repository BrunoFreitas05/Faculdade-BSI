var http = require('http');
//var dt = require ('./testeModulo');
var url = require('url');


const protocol = "http"
const hostName = "127.0.0.1";
const port = "3000";

http.createServer(function(req, res){
    res.writeHead(200,{'Content-Type' :'text/html'});
    var q =url.parse(req.url, true).query;
    var txt = q.ano + " " + q.mes;
    //res.write(req.url);
    res.end(txt);
}).listen(3000);

  console.log(`Servidor Rodando em ${protocol}://${hostName}:${port}`);
