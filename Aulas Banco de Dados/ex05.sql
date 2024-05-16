create database ex05;
use ex05;

create table departamento(
codigo int unsigned not null,
descricao varchar(50) not null,
constraint pk_departamento primary key(codigo)
);

create table funcionario(
registro int unsigned not null,
nome varchar(80) not null,
data_de_nascimento date not null,
codigo int unsigned null,
constraint pk_funcionario primary key(registro),
constraint fk_departamento foreign key (codigo) references departamento(codigo)
);

alter table funcionario
add salario decimal(8,2);

drop table funcionario;
 
