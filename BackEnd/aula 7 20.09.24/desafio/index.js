import express from 'express';
const server = express();

const products_db = [
  { id: 1, descricao: "meia", preco: 9.99, estoque: 500, disponivel: true },
  { id: 2, descricao: "calça", preco: 310.00, estoque: 0, disponivel: false },
  { id: 3, descricao: "saia", preco: 150.69, estoque: 105, disponivel: true },
  { id: 4, descricao: "camiseta", preco: 55.99, estoque: 768, disponivel: true },
  { id: 5, descricao: "blusa", preco: 250.00, estoque: 50, disponivel: true },
]

server.use(express.json());

server.use((req, res, next) => {
  res.header("Access-Control-Allow-Methods",
    "GET, POST, PUT, DELETE");
    next();
})

server.get("/products", (req, res) => {
  return res.status(200).json(products_db);
});

server.get("/products/:id", (req, res) => {
  const id = parseInt(req.params.id);

  if (id) {
    const product = products_db.find(product => product.id === id);
    if (product) {
      return res.status(200).json({
        id: product.id,
        descricao: product.descricao,
        preco: product.preco,
        estoque: product.estoque,
        disponivel: product.disponivel
      });
    } else {
      return res.status(404).json({
        message: `productId ${id} wasn't found`
      });
    }
  }
})

server.post("/products", (req, res) => {
  const { descricao, preco, estoque, disponivel } = req.body;

  if (!(descricao || preco || estoque)) {
    return res.status(400).json({ message: "Bad request" })
  }

  const id = products_db.length ? products_db[products_db.length - 1].id + 1 : 1;
  const newProduct = { id, descricao, preco, estoque, disponivel };

  products_db.push(newProduct);
  return res.status(201).json(newProduct);
});

server.put("/products/:id", (req, res) => {
  const id = parseInt(req.params.id);
  const { descricao, preco, estoque, disponivel } = req.body;

  const productIndex = products_db.findIndex(product => product.id === id);
  if (productIndex !== -1) {
    products_db[productIndex] = { id, descricao, preco, estoque, disponivel };
    return res.status(200).json(products_db[productIndex]);
  } else {
    return res.status(404).json({
      message: `productId ${id} wasn't found`
    });
  }
});

server.delete("/products/:id", (req, res) => {
  const id = parseInt(req.params.id);
  const productIndex = products_db.findIndex(product => product.id === id);

  if (productIndex !== -1) {
    const deletedProduct = products_db.splice(productIndex, 1);
    return res.status(200).json( { "deleted product": deletedProduct[0] });
  } else {
    return res.status(404).json({
      message: `ProductId ${id} wasn't found`
    });
  }
});

server.listen(3000, () => {
  console.log("http://127.0.0.1:3000/products");
});