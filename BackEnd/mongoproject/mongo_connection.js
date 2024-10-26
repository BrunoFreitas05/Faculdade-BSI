const {MongoClient, ServerApiVersion} = require("mongodb");

// Definir string de coneção
const uri = "mongodb://localhost:27017/";

// Criar um objeto MongoClient com as opções setadas
const client = new MongoClient(uri, {
    serverApi: {
        version: ServerApiVersion.v1,
        strict: true,
        deprecationErrors: true,
    }
});

async function run(){
    try{
        // conectar ao servidor
        await client.connect();

        // Enviar um ping para confirmar a conexao
        await client.db("mydb").command({ping: 1});
        console.log("Conexao bem sucedida");

    } finally {
        //fechar a conexao
        await client.close();
    }
}

run().catch(console.dir);