CREATE SCHEMA aula8;
USE aula8;

CREATE TABLE departamentos (
	codigo_dpto INT UNSIGNED NOT NULL,
    descricao_dpto VARCHAR(50) NOT NULL,
    CONSTRAINT PK_departamento PRIMARY KEY (codigo_dpto)
) ENGINE InnoDB;

DESCRIBE departamentos;

INSERT INTO departamentos (codigo_dpto, descricao_dpto) 
VALUES
(3, "Almoxaficado"),
(4, "Vendas"),
(5,"Compras"),
(6,"Limpeza");

SELECT * FROM departamentos;

UPDATE departamentos
SET descricao_dpto = "Almoxarifado"
WHERE codigo_dpto = 3;


