-- MySQL Script generated by MySQL Workbench
-- Thu Sep 14 12:48:22 2017
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema emails
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema emails
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `emails` DEFAULT CHARACTER SET utf8 ;
USE `emails` ;

-- -----------------------------------------------------
-- Table `emails`.`emails`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `emails`.`emails` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
