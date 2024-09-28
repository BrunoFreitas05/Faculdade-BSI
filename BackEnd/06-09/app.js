import { createServer } from "http";
import { readFile } from "fs";
import { parse } from "url";
 
const protocol = "http"
const hostName = "127.0.0.1";
const port = "8080";
 
const server = createServer((req, res) => {
  let currentPathname = parse(req.url).pathname.slice(1);
 
  readFile(`${currentPathname}.html`, (err, data) => {
    if (data) {
      res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
      res.write(data);
    } else {
      res.writeHead(404, { "Content-Type": "text/html; charset=utf-8" });
      res.write("page not found");
    }
  });
});
 
server.listen(port, hostName, () => {
  console.log(`ta aq: ${protocol}://${hostName}:${port}/front`);
});