CREATE DATABASE ex06;
USE ex06;

-- 1
CREATE TABLE cidade(
idcidade INT NOT NULL,
descricao VARCHAR(50) NOT NULL,
CONSTRAINT PK_Cidade PRIMARY KEY (idcidade)
) ENGINE= InnoDB;

CREATE TABLE departamento(
iddepartamento INT NOT NULL,
descricao VARCHAR(45) NOT NULL,
telefone VARCHAR (15),
idcidade INT NOT NULL,
CONSTRAINT PK_Departamento PRIMARY KEY (iddepartamento),
CONSTRAINT FK_Departamento_Cidade 
FOREIGN KEY(idcidade) REFERENCES cidade (idcidade)
) ENGINE= InnoDB;

CREATE TABLE funcionario(
idfuncionario int not null,
nome varchar(80) not null,
nascimento date not null,
sexo char(1) not null,
admissao datetime,
salario decimal(8,2),
iddepartamento int not null,
constraint pk_funcionario primary key(idfuncionario),
constraint fk_funcionario_departamento
foreign key(iddepartamento) references departamento(iddepartamento)
) engine=innoDB;





