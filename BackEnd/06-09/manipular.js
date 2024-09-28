const fs = require('fs');

// // cria arquivo e adiciona conteúdo ou apenas edita arquivo e adiciona conteúdo
// fs.appendFile("teste.txt", "askjsadkjdkvfjndnjffkjdfkndfkdfjvfk\n", (err) => {
//   if (err) {
//     console.log("erro ao criar ou editar arquivo")
//   } else {
//     console.log("arquivo salvo")
//   }
// });

// // abre e loga conteúdo do arquivo
// fs.readFile("teste.txt", "utf8", (err, data) => {
//   if (err) {
//     console.log("erro ao abrir arquivo")
//   } else {
//     console.log("conteúdo do arquivo:")
//     console.log(data);
//   }
// });

// // sobrescreve ou cria
// fs.writeFile("nexiste.txt", "novo arquivo aq", (err) => {
//   if (err) {
//     console.log("erro ao criar")
//   } else {
//     console.log("criou novo arquivo")
//   }
// })

// delete
fs.unlink("nexiste.txt", (err) => {
  if (err) {
    console.log("erro ao deletar")
  } else {
    console.log("deletou arquivo teste.txt")
  }
});

// // rename
// fs.rename("teste.txt", "testerename.txt", (err) => {
//   if (err) {
//     console.log("erro ao renomear")
//   } else {
//     console.log("teste.txt renomeado para testerename.txt");
//   }
// })