create database Pessoas;
drop database Nomes;
use Pessoas;
CREATE TABLE nomes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    primeiro_nome VARCHAR(50),
    ultimo_nome VARCHAR(50),
    idade INT,
    email VARCHAR(100),
    data_de_nascimento DATE
);
INSERT INTO nomes (primeiro_nome, ultimo_nome, idade, email, data_de_nascimento) VALUES
    ('João', 'Silva', 25, 'joao.silva@example.com', '1999-05-15'),
    ('Maria', 'Santos', 30, 'maria.santos@example.com', '1994-08-22'),
    ('Pedro', 'Oliveira', 35, 'pedro.oliveira@example.com', '1989-11-10'),
    ('Ana', 'Costa', 28, 'ana.costa@example.com', '1996-03-28'),
    ('Carlos', 'Pereira', 40, 'carlos.pereira@example.com', '1982-09-17'),
    ('Mariana', 'Rodrigues', 22, 'mariana.rodrigues@example.com', '2002-01-08'),
    ('Rafael', 'Fernandes', 33, 'rafael.fernandes@example.com', '1989-07-03'),
    ('Camila', 'Gonçalves', 27, 'camila.goncalves@example.com', '1997-12-14'),
    ('Lucas', 'Martins', 31, 'lucas.martins@example.com', '1993-06-20'),
    ('Fernanda', 'Almeida', 29, 'fernanda.almeida@example.com', '1995-04-25'),
    ('Gustavo', 'Vieira', 26, 'gustavo.vieira@example.com', '1998-10-30'),
    ('Juliana', 'Lima', 34, 'juliana.lima@example.com', '1988-02-12'),
    ('Rodrigo', 'Rocha', 32, 'rodrigo.rocha@example.com', '1990-08-05'),
    ('Vanessa', 'Nascimento', 23, 'vanessa.nascimento@example.com', '2001-11-19'),
    ('Felipe', 'Cruz', 37, 'felipe.cruz@example.com', '1987-06-14');
    select * from Nomes;
