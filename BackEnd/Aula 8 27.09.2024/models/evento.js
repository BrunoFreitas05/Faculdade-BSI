const mongoose = require ('mongoose')
 
//Schema
const EventSchema = new mongoose.Schema({
    titulo:{
        type: String,
        required: true
    },
    data:{
        type: Date,
        required: true
    },
    organizador:{
        type: String,
        required: true
    },
    preço:{
        type: Number,
        required: true,
    },
    localizacao:{
       type: String,
        required: true,
    },
    descricao:{
        type: String,
        required: true
        },
    },  
    {timestamps : true}
);

const Evento = mongoose.model('evento', EventSchema);

module.exports = Evento;