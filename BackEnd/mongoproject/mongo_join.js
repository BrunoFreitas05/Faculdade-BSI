const { MongoClient } = require("mongodb");
// Replace the placeholder with your connection string.
const uri = "mongodb://localhost:27017/";
const client = new MongoClient(uri);
async function run() {
  try {
    // Configurar DB e coleções a serem utilizadas
    const aggDB = client.db("mydb");
    const productsColl = aggDB.collection("products");
    const ordersColl = aggDB.collection("orders");

    const pipeline = [];
    const embedded_pl = [];
    
    // Definir nomes alternativos para os campos das collections
    embedded_pl.push({
        $match:{
            $expr: {
                $and: [
                    {$eq: ["$product_name", "$$prdname"]},
                    {$eq: ["$product_variation", "$$prdvartn"]},
                ],
            },
        },
    });

    // remover campos desnecessários como id, nomo do produto e variação
    embedded_pl.push({
        $unset:["_id", "product_name", "productvariation"],
    });

    // 
    pipeline.push({
        $lookup: {
            from: "orders",
            let: {
                prdname: "$name",
                prdvartn: "$variation"
            },
            pipeline: embedded_pl,
            as: "orders",
        },
    });



    pipeline.push({
        $unset: ["_id", "description"],
    });



    // Executar o pipeline
    const aggregationResult = await productsColl.aggregate(pipeline);
    
   
    for await (const document of aggregationResult) {
      console.log(document);
    }
  } finally {
    await client.close();
  }
}
run().catch(console.dir);