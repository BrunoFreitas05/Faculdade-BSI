CREATE DATABASE aula7;
USE aula7;

CREATE TABLE departamento(
codigo INT UNSIGNED NOT NULL,
descricao VARCHAR(50) NOT NULL,
constraint pk_departamento primary key(codigo) /*Obrigatorio em todos os bancos.*/
);

-- inserindo registros(exemplos)
insert into departamento(codigo,descricao) values(101,'Tecnologia da informação');
insert into departamento(codigo,descricao) values(103,'Recursos Humanos');
insert into departamento(codigo,descricao) values(102,'Vendas');1
insert into departamento values(104,'Compras');
insert into departamento values(106,'Compras');
insert into departamento(descricao,codigo) values('Almoxarifado',105);

-- exemplos declaracao que exibe o conteudo
select * from departamento;
select descricao from departamento;
select distinct descricao from departamento; -- Elimina colunas repitdas


create table funcionario(
id int not null,
nome varchar(80) not null,
sexo char(1) null,
nascimento date null,
salario decimal(8,2) null,
cod_depto int unsigned not null,
constraint pk_funcionario primary key (id),
constraint chk_salario check(salario>0),
constraint fk_departamento foreign key
(cod_depto) references departamento(codigo)
);



create table produto(
codigo int unsigned not null primary key,
descricao varchar(40)
);



create table nfe(
numero int unsigned not null primary key,
emissao date
);



create table item_nfe(
codigo int unsigned not null,
numero int unsigned not null,
quantidade int not null,
constraint pk_item_nfe primary key (codigo,numero),
constraint fk_item_nfe_produto foreign key(codigo) references produto (codigo),
constraint fk_item_nfe_nfe foreign key(numero) references nfe (numero)
);

insert into funcionario (id,nome,sexo,nascimento,salario,cod_depto) values
(1,'Bruno Marques Freitas','M','2004-08-05','2000','101'),
(2,'Samuel Pereira Barreto','M','2004-04-11','3000','101'),
(3,'Caio Issao','M','2004-08-05','5000','101'),
(4,'Andrei De Oliveira','M','2004-08-05','4000','101');
insert into funcionario (id,nome,cod_depto) values
(5,'Beto',102);

select * from funcionario;


