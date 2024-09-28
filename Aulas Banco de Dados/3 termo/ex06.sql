-- CROSS JOIN
SELECT *
   FROM pessoa
   JOIN cidade;
   
   --
   SELECT *
      FROM pessoa, cidade;
      
      -- JOIN
      SELECT *
         FROM  pessoa
         JOIN cidade
           ON (pessoa.cod_cidade = cidade.cod_cidade);
           
	-- Natural join
    SELECT pessoa.*, cidade.local
	  FROM pessoa
      NATURAL JOIN cidade;
      
      ALTER TABLE cidade
      ADD COLUMN nome VARCHAR(30);