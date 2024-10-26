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

        // Criar um documento a ser inserido
        const doc = {
            nome: "Afonso Liberato",
            idade: 35,
            email: "al@univem.edu.br"
        }

        // Inserir documento na coleção 
        const result = await pessoas.insertOne(doc);

        // Imprimir o ID do documento inserido
        console.log(`Documento inserido. id: ${result.insertedId}`);


    } finally {
        // fechar a conexão
        await client.close();

    }
    
}

// Inserir vários documentos (registros)
async function run2(){
    try{
        // setar database e collection que será usada nessa função
        const database = client.db("mydb");
        const pessoas = database.collection("pessoas");

        // Criar Array com os documentos a serem inseridos
        const docs = [
            {nome: "Marina Sabrina Campos", idade: 52, email: "marinasabrinacampos@manjubinhafilmes.com.br"},
            {nome: "Luiz Filipe Figueiredo", idade:58 , email: "luiz_figueiredo@gripoantonin.com"},
            {nome: "Vitória Isabela da Mota", idade: 44, email: "vitoria_damota@cernizza.com.br"},
            {nome: "Manuel Márcio Mateus Carvalho", idade: 31, email: "manuel.marcio.carvalho@fojsc.unesp.br"},
            {nome: "Emily Regina Almeida", idade: 32, email: "emily_regina_almeida@elimco.com"}
        ];

        // Prover documentos adicionais em caso de falha
        const options = {ordered: true};

        // Executar a operação de inserir vários documentos
        const result = await pessoas.insertMany(docs, options);

        // Retornar o resultado
        console.log(`${result.insertedCount} documentos foram inseridos`);
    }finally{
        await client.close();
    }
}


// rodar a função
//run().catch(console.dir);
run2().catch(console.dir);