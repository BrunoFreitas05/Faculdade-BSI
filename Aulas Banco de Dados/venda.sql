-- MySQL Script generated by MySQL Workbench
-- Sun Apr  7 19:47:21 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Cliente` (
  `idClientes` INT NOT NULL,
  `CPF_CNPJ` VARCHAR(20) NOT NULL,
  `RG/IE` VARCHAR(20) NOT NULL,
  `Nome_RazaoSocial` VARCHAR(45) NOT NULL,
  `Endereco` VARCHAR(200) NOT NULL,
  `Telefone` VARCHAR(45) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idClientes`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Produto` (
  `idProduto` INT NOT NULL,
  `Codigo` VARCHAR(45) NOT NULL,
  `Descricao` VARCHAR(200) NOT NULL,
  `ValorUnitario` DECIMAL(10,2) NOT NULL,
  `Percentual_icms` DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (`idProduto`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Venda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Venda` (
  `idVenda` INT NOT NULL,
  `DataTransacao` DATE NOT NULL,
  `FormaPagamento` VARCHAR(45) NOT NULL,
  `ValorDesconto` DECIMAL(10,2) NOT NULL,
  `ValorTotal` DECIMAL(10,2) NOT NULL,
  `Cliente_idClientes` INT NOT NULL,
  PRIMARY KEY (`idVenda`, `Cliente_idClientes`),
  INDEX `fk_Venda_Cliente1_idx` (`Cliente_idClientes` ASC) VISIBLE,
  CONSTRAINT `fk_Venda_Cliente1`
    FOREIGN KEY (`Cliente_idClientes`)
    REFERENCES `mydb`.`Cliente` (`idClientes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Venda_Produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Venda_Produto` (
  `Produto_idProduto` INT NOT NULL,
  `Venda_idVenda` INT NOT NULL,
  `Venda_Cliente_idClientes` INT NOT NULL,
  `Quantidade` INT NOT NULL,
  `ValorTotalProduto` INT NOT NULL,
  PRIMARY KEY (`Produto_idProduto`, `Venda_idVenda`, `Venda_Cliente_idClientes`),
  INDEX `fk_Produto_has_Venda_Venda1_idx` (`Venda_idVenda` ASC, `Venda_Cliente_idClientes` ASC) VISIBLE,
  INDEX `fk_Produto_has_Venda_Produto1_idx` (`Produto_idProduto` ASC) VISIBLE,
  CONSTRAINT `fk_Produto_has_Venda_Produto1`
    FOREIGN KEY (`Produto_idProduto`)
    REFERENCES `mydb`.`Produto` (`idProduto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Produto_has_Venda_Venda1`
    FOREIGN KEY (`Venda_idVenda` , `Venda_Cliente_idClientes`)
    REFERENCES `mydb`.`Venda` (`idVenda` , `Cliente_idClientes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`CreditoPréAprovado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`CreditoPréAprovado` (
  `Credito` DECIMAL(10,2) NOT NULL,
  `Cliente_idClientes` INT NOT NULL,
  PRIMARY KEY (`Cliente_idClientes`),
  CONSTRAINT `fk_CreditoPréAprovado_Cliente1`
    FOREIGN KEY (`Cliente_idClientes`)
    REFERENCES `mydb`.`Cliente` (`idClientes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
