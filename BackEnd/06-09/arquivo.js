var fs = require('fs');
var http = require('http');
 
//Criar servidor HTTP
http.createServer(function (req, res){
    fs.readFile('index.html', function(err, data){
        res.writeHead(200, {'Content-type': 'text/html'});
        res.write(data);
        return res.end();
        })
}).listen(8080);