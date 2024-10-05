require('dotenv').config();

//Importa framework express,ejs,mangoose para a aplicação
const express = require('express');
const ejs = require('ejs');
const mongoose = require('mongoose');
const Evento = require('./models/evento.js')

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


app.post('/submit-evento', (req,res) =>{
    const evento = new Evento(req.body);
    evento.save()
        .then((result)=>{
            res.redirect('/');
        })
        .catch((err) => {
            console.error(err);
        });
});

app.get('/', (req,res) =>{
    Evento.find()
        .then((result)=>{
            res.render('index', {titile:'Todos eventos', events: result})
        })
        .catch((err) => {
            console.error(err);
        });
});


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
 