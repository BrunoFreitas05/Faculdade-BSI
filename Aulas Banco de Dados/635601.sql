-- Exercicio 01 
select estado.uf as 'UF',coalesce(cidade.nome, 'Sem Cidade') as 'Cidade', estado.nome as 'Estado'
from estado 
left join cidade on cidade.uf = estado.uf;

select * from estado;
select *from cidade;

-- Exercicio 2
select ceps.cep, ceps.logradouro, bairro.descricao as 'Bairro', cidade.nome as 'Cidade', cidade.uf
from ceps
join bairro on bairro.idbairro = ceps.idbairro
join cidade on cidade.idcidade = bairro.idcidade
where cidade.nome = 'Marília';

-- Exercicio 3
select cliente.nome, count(nfe.numero) as 'Notas Fiscais'
from cliente
left join nfe on cliente.idcliente = nfe.idcliente
group by cliente.nome;

-- Exercicio 4
select nfe.numero, truncate(sum(produto.valor_unitario * item_nfe.quantidade), 2) as 'Valor Notas Joca'
from nfe
join item_nfe on nfe.numero = item_nfe.numero
join produto on item_nfe.idproduto = produto.idproduto
where nfe.idcliente =1
group by nfe.numero;

-- Exercicio 5
SELECT cliente.nome AS nome_cliente, ceps.logradouro, cliente.numero, cliente.complemento, bairro.descricao AS bairro, cidade.nome AS cidade, estado.nome AS estado
FROM nfe
JOIN cliente ON nfe.idcliente = cliente.idcliente
JOIN ceps ON cliente.cep = ceps.cep
JOIN bairro ON ceps.idbairro = bairro.idbairro
JOIN cidade ON bairro.idcidade = cidade.idcidade
JOIN estado ON cidade.uf = estado.uf
WHERE nfe.numero = 4;


-- Exercicio 6
SELECT cliente.nome AS nome_cliente, nfe.numero AS numero_nota, nfe.data AS data_nota, produto.descricao AS descricao_produto, item_nfe.quantidade, produto.valor_unitario, (item_nfe.quantidade * produto.valor_unitario) AS valor_total_produto
FROM nfe
JOIN cliente ON nfe.idcliente = cliente.idcliente
JOIN item_nfe ON nfe.numero = item_nfe.numero
JOIN produto ON item_nfe.idproduto = produto.idproduto
WHERE nfe.numero = 1;

-- Exercicio 7
SELECT cliente.nome AS nome_cliente, produto.valor_unitario, item_nfe.quantidade, (item_nfe.quantidade * produto.valor_unitario) AS valor_total
FROM item_nfe
JOIN produto ON item_nfe.idproduto = produto.idproduto
JOIN nfe ON item_nfe.numero = nfe.numero
JOIN cliente ON nfe.idcliente = cliente.idcliente
WHERE produto.idproduto = 1;

-- Exercicio 8
SELECT cidade.nome AS nome_cidade, estado.uf, estado.nome AS nome_estado
FROM cidade
JOIN estado ON cidade.uf = estado.uf;

-- Exercicio 9
SELECT MAX(produto.valor_unitario) AS maior_valor_unitario
FROM produto;

-- Exercicio 10
SELECT UPPER(LEFT(cliente.nome, 3)) AS iniciais_nome_cliente
FROM cliente;




