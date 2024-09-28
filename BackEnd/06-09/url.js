var url = require('url');
var adr ='http://localhost:8080/default.html?ano=2024&mes=setembro';
var q = url.parse(adr,true);
 
console.log('host:'+q.host);
console.log('path:'+q.pathname);
console.log('search:'+q.search);
 
 
var qdata = q.query;
 
console.log('mes:'+qdata.mes+
    'ano:'+qdata.ano);