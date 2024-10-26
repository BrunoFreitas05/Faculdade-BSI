const {MongoClient, ServerApiVersion} = require("mongodb");

// Definir string de coneção
const uri = "mongodb://localhost:27017/";

// Criar cliente e conectar ao mongoDB
const client = new MongoClient(uri);


// Localizar 1 documento
async function run(){

    try{
        // conectar ao banco de dados e criara uma coleção (tabela)
        const database = client.db("mydb");
        const pessoas = database.collection("pessoas");

        // Encontrar uma pessoa de nome "Afonso Liberato"
        const query = {nome: "Afonso Liberato"};

        // definir opções de como retornar a busca
        const options = {
            // retornar apenas o nome e a idade
            projection: {_id:0, nome:1, idade:1},
        };

        // executar a query
        const pessoa = await pessoas.findOne(query, options);

        // Imprimir o resultado
        console.log(pessoa);

    } finally {
        // fechar a conexão
        await client.close();

    }
    
}


// Localizar todos os documentos cadastrados
async function run2(){

    try{
        // conectar ao banco de dados e criara uma coleção (tabela)
        const database = client.db("mydb");
        const pessoas = database.collection("pessoas");

        // Definir query de busca
        //const query = {nome: /^A/}; // somente com nomes iniciados com A (case sensitive)   
        //const query = {idade: {$lt: 40}}; // somente com idade menor que 40
        const query = {}; // Todos os elementos

        
        // definir opções de como retornar a busca
        const options = {
            // ordenar em ordem alfabetica crescente
            sort: {idade: 1},
            // retornar apenas o nome e a idade
            projection: {_id:0, nome:1, idade:1},

            limit: 3,
        };

        /*
        { name: 1 } // ascending
        { name: -1 } // descending  
        */

        
        // executar a query
        const cursor = pessoas.find(query, options);

        // Imprimir o resultado caso não seja encontrado documentos
        if ((await pessoas.countDocuments({})) === 0) {
            console.log("Nenhum documento encontado");
        }

        // Imprimir documentos encontrados
        for await (const doc of cursor) {
            console.dir(doc);
        }

    } finally {
        // fechar a conexão
        await client.close();

    }
    
}


// rodar a função
run2().catch(console.dir);
