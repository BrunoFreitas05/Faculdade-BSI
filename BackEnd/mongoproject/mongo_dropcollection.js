const {MongoClient, ServerApiVersion} = require("mongodb");

// Definir string de coneção
const uri = "mongodb://localhost:27017/";

// Criar cliente e conectar ao mongoDB
const client = new MongoClient(uri);

async function run(){

    try{
        // conectar ao banco de dados e criara uma coleção (tabela)
        const database = client.db("mydb");
        const pessoas = database.collection("pessoas");



        // Deletar o primeiro documento da coleção que atender ao requisito da query
        //const query = {nome: "Afonso Liberato"};
        const result = await database.dropCollection("pessoas");

        // Imprimir uma mensagem indicando a operação realizada

        console.log("Collection deletada")
        


    } finally {
        // fechar a conexão
        await client.close();

    }
    
}

// rodar a função
run().catch(console.dir);
