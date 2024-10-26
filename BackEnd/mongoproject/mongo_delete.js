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
        const query = {nome: "Afonso Liberato"};
        const result = await pessoas.deleteOne(query);

        // Imprimir uma mensagem indicando a operação realizada

        if(result.deletedCount === 1){
            console.log("Documento excluído!");
        } else {
            console.log("nenhum documento encontrato.")
        }
        


    } finally {
        // fechar a conexão
        await client.close();

    }
    
}

async function run2(){

    try{
        // conectar ao banco de dados e criara uma coleção (tabela)
        const database = client.db("mydb");
        const pessoas = database.collection("pessoas");

        // Deletar os documentos que atendam a expressão regular
        const query = {email: {$regex:".br"}};
        const result = await pessoas.deleteMany(query);

        // Imprimir uma mensagem indicando a operação realizada
        console.log("Deletado "+ result.deletedCount + " documentos");
        


    } finally {
        // fechar a conexão
        await client.close();

    }
    
}




// rodar a função
//run().catch(console.dir);
run2().catch(console.dir);