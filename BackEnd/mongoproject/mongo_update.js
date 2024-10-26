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

        // Criar um filtro: nome deve ser igual a "Afonso Liberato"
        const filter = {nome: "Afonso Liberato"};

        // seta a opção para adicionar o dado na colection caso não exita
        const options = {upsert: true};

        // Especifica o campo e o novo valor a ser atualizado
        const updateDoc = {
            $set: {
                nome: "Afonso Lucas Liberato"
            },
        };

        // atualizar o primeiro documento que atender ao filtro
        const result = await pessoas.updateOne(filter, updateDoc, options);

        // Imprimir uma mensagem indicando a operação realizada
        console.log(
            `${result.matchedCount} documentos combinam com o filtro, atualizados ${result.modifiedCount} documentos`,
        );
        


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

        // Criar um filtro: nome deve ser igual a "Afonso Liberato"
        const filter = {email: {$regex:".br"}};

        // Especifica o campo e o novo valor a ser atualizado
        const updateDoc = {
            $set: {
                email: "teste@teste.com"
            },
        };

        // atualizar o primeiro documento que atender ao filtro
        const result = await pessoas.updateMany(filter, updateDoc);

        // Imprimir uma mensagem indicando a operação realizada
        console.log(
            `${result.matchedCount} documentos combinam com o filtro, atualizados ${result.modifiedCount} documentos`,
        );
        


    } finally {
        // fechar a conexão
        await client.close();

    }
    
}


async function run3(){

    try{
        // conectar ao banco de dados e criara uma coleção (tabela)
        const database = client.db("mydb");
        const pessoas = database.collection("pessoas");

        // Criar um filtro: nome deve ser igual a "Afonso Liberato"
        const query = {nome: {$regex: "Afonso"}};

        // Especifica o campo e o novo valor a ser atualizado
        const replacement = {
            nome: "José Maria Vianey"
        };

        // atualizar o primeiro documento que atender ao filtro
        const result = await pessoas.replaceOne(query, replacement);

        // Imprimir uma mensagem indicando a operação realizada
        console.log(
            `${result.matchedCount} documentos combinam com o filtro, atualizados ${result.modifiedCount} documentos`,
        );
        


    } finally {
        // fechar a conexão
        await client.close();

    }
    
}

// rodar a função
//run().catch(console.dir);
//run2().catch(console.dir);
run3().catch(console.dir);