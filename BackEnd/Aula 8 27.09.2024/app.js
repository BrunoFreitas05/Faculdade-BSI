//Importa framework express,ejs,mangoose para a aplicação
const express = require('express');
const ejs = require('ejs');
const mongoose = require('mongoose');
const Evento = require('./models/evento.js')

//String de conexao com o banco Mongo
const dbURL = "mongodb+srv://brunomfreitas014:051973@brunoclauster.9evnd.mongodb.net/?retryWrites=true&w=majority&appName=BrunoClauster";
//Inicializar o express na aplicação
const app = express();

//Setar ejs como motor de visualização de aplicação
app.set('view engine', 'ejs');

//Criar rota de teste

app.get('/',(req,res) =>{
    res.send('Hello World');
});

// app.listen(3000,()=>{
//     console.log('Servidor rodando na porta 3000');
// });


mongoose
.connect(dbURL)
.then((result)=>{
    console.log('Conectado ao banco de dados')
    app.listen(3000,()=>{
        console.log('Servidor rodando na porta 3000')
    });
})
.catch(err => {
    console.log('Não foi possível conectar',err);
})
 