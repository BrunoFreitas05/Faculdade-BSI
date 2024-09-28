const express = require('express');

const server = express();

const users = ["Dalton", "Nicolas", "Varella"];

server.use(express.json());

server.use((req, res, next) => {
  res.header("Access-Control-Allow-Methods",
    "GET, POST, PUT, DELETE");
    next();
})

// API Retorna uma lista de users quando requisitado
server.get('/users', (req, res) =>{
    return res.json(users);

});

server.get('/users/:index', (req, res) => {

    //const nome = req.query.nome;
    //const id = req.params.id;
    const {index} = req.params;

    //return res.json(users[index]);

    return res.json({
        nome: users[index],
        //mensagem: `Buscando usuario ${id}`
    });
});

server.post("/users", (req, res) => {
    const {name} = req.body;
    users.push(name);

    return res.json(users);
})

server.put("/users/:index", (req, res) => {
    const {index} = req.params;
    const {name} = req.body;

    users[index] = name;

    return res.json(users);
})

server.delete("/users/:index", (req, res) => {
    const {index} = req.params;

    users.splice(index, 1);

    return res.json({ message: "deleted "});
})

server.listen(3001);