import express from 'express';
const server = express();

const db = [
  { id: 1, nome: "samu", idade: 20 },
  { id: 2, nome: "bubi", idade: 21 },
  { id: 3, nome: "didi", idade: 17 },
  { id: 4, nome: "dédé", idade: 170 },
]

server.use(express.json());

server.use((req, res, next) => {
  res.header("Access-Control-Allow-Methods",
    "GET, POST, PUT, DELETE");
    next();
})

server.get("/users", (req, res) => {
  return res.status(200).json(db);
});

server.get("/users/:id", (req, res) => {
  const id = parseInt(req.params.id);

  if (id) {
    const user = db.find(user => user.id === id);
    if (user) {
      return res.status(200).json({
        id: user.id,
        nome: user.nome,
        idade: user.idade,
      });
    } else {
      return res.status(404).json({
        message: `UserId ${id} wasn't found`
      });
    }
  }
})

server.post("/users", (req, res) => {
  const { nome, idade } = req.body;
  // const nome = req.body.nome;
  // const idade = req.body.idade;

  const id = db.length ? db[db.length - 1].id + 1 : 1;
  const newUser = { id, nome, idade };

  db.push(newUser);
  return res.status(201).json(newUser);
});

server.put("/users/:id", (req, res) => {
  const id = parseInt(req.params.id);
  const { nome, idade } = req.body;

  const userIndex = db.findIndex(user => user.id === id);
  if (userIndex !== -1) {
    db[userIndex] = { id, nome, idade };
    return res.status(200).json(db[userIndex]);
  } else {
    return res.status(404).json({
      message: `UserId ${id} wasn't found`
    });
  }
});

server.delete("/users/:id", (req, res) => {
  const id = parseInt(req.params.id);
  const userIndex = db.findIndex(user => user.id === id);

  if (userIndex !== -1) {
    const deletedUser = db.splice(userIndex, 1);
    return res.status(200).json( { "deleted user": deletedUser[0] });
  } else {
    return res.status(404).json({
      message: `UserId ${id} wasn't found`
    });
  }
});

server.listen(3000, () => {
  console.log("http://127.0.0.1:3000/users");
});