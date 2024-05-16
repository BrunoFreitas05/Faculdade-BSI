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
-- Table `mydb`.`Grupo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Grupo` (
  `idGrupo` INT NOT NULL,
  `Nome_Grupo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idGrupo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Produto` (
  `idProduto` INT NOT NULL,
  `Nome_Produto` VARCHAR(45) NOT NULL,
  `Grupo_idGrupo` INT NOT NULL,
  PRIMARY KEY (`idProduto`),
  INDEX `fk_Produto_Grupo1_idx` (`Grupo_idGrupo` ASC) VISIBLE,
  CONSTRAINT `fk_Produto_Grupo1`
    FOREIGN KEY (`Grupo_idGrupo`)
    REFERENCES `mydb`.`Grupo` (`idGrupo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Almoxarifado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Almoxarifado` (
  `idAlmoxarifado` INT NOT NULL,
  `Nome_Almoxarifado` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idAlmoxarifado`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Estoque`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Estoque` (
  `Produto_idProduto` INT NOT NULL,
  `Almoxarifado_idAlmoxarifado` INT NOT NULL,
  `Quantidade` INT NOT NULL,
  `Valor_unitario` DECIMAL(8,2) NOT NULL,
  `Data_Cadastro` DATE NOT NULL,
  PRIMARY KEY (`Produto_idProduto`, `Almoxarifado_idAlmoxarifado`),
  INDEX `fk_Produto_has_Almoxarifado_Almoxarifado1_idx` (`Almoxarifado_idAlmoxarifado` ASC) VISIBLE,
  INDEX `fk_Produto_has_Almoxarifado_Produto_idx` (`Produto_idProduto` ASC) VISIBLE,
  CONSTRAINT `fk_Produto_has_Almoxarifado_Produto`
    FOREIGN KEY (`Produto_idProduto`)
    REFERENCES `mydb`.`Produto` (`idProduto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Produto_has_Almoxarifado_Almoxarifado1`
    FOREIGN KEY (`Almoxarifado_idAlmoxarifado`)
    REFERENCES `mydb`.`Almoxarifado` (`idAlmoxarifado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Telefone`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Telefone` (
  `Numero_telefone` VARCHAR(15) NOT NULL,
  `Almoxarifado_idAlmoxarifado` INT NOT NULL,
  PRIMARY KEY (`Almoxarifado_idAlmoxarifado`, `Numero_telefone`),
  INDEX `fk_Telefone_Almoxarifado1_idx` (`Almoxarifado_idAlmoxarifado` ASC) VISIBLE,
  CONSTRAINT `fk_Telefone_Almoxarifado1`
    FOREIGN KEY (`Almoxarifado_idAlmoxarifado`)
    REFERENCES `mydb`.`Almoxarifado` (`idAlmoxarifado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
